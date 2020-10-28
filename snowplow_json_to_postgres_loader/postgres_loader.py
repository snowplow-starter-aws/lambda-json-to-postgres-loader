import logging
import re
import psycopg2

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def to_snake_case(str):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in str]).lstrip('_')


def is_not_context_field(element):
    return not is_context_field(element)


def is_context_field(element):
    return element.startswith("contexts")


def partition(cond, inputList):
    a, b = [], []
    for item in inputList:
        target = a if cond(item) else b
        target.append(item)
    return a, b


def to_string(value):
    if isinstance(value, int) or isinstance(value, float):
        return str(value)
    else:
        return f"'{value}'"


class Context:
    # contexts__com_snowplowanalytics_snowplow__ua_parser_context__1
    SCHEMA_REGEX = re.compile(r"^(\w+)__(\w+)__(\w+)__(\d+)")

    def __init__(self, vendor, name, format, version, event_id, collector_tstamp, objs):
        # atomic.my_custom_context_table.root_id = atomic.events.event_id
        self.schema_vendor = vendor
        self.schema_name = name
        self.schema_format = format
        self.schema_version = version
        self.root_id = event_id
        self.root_tstamp = collector_tstamp
        self.ref_root = 'tbd'
        self.ref_tree = 'tbd'
        self.ref_parent = 'tbd'
        self.objs = objs

    @staticmethod
    def create(name, objs, event_id, collector_tstamp):
        # contexts__com_snowplowanalytics_snowplow__ua_parser_context__1
        match = re.match(Context.SCHEMA_REGEX, name)
        if match:
            vendor = match.group(2)
            name = match.group(3)
            version = match.group(4)
            return Context(vendor, name, 'jsonschema', str(version), event_id, collector_tstamp, objs)
        else:
            return None

    def insert_stmts(self):
        return [self._insert_stmt(obj) for obj in self.objs]

    def _insert_stmt(self, obj):
        table_name = f'{self.schema_vendor}_{self.schema_name}_{self.schema_version}'
        parameters = list(obj.keys())
        values = ['schema_vendor', 'schema_name', 'schema_format', 'schema_version',
                  'root_id', 'root_tstamp', 'ref_root', 'ref_tree', 'ref_parent'
                  ] + [to_snake_case(p) for p in parameters]
        assignments = [self.schema_vendor, self.schema_name, self.schema_format, self.schema_version,
                       self.root_id, self.root_tstamp, self.ref_root, self.ref_tree, self.ref_parent
                       ] + [obj[p] for
                            p in
                            parameters]

        joined_values = ','.join(values)
        joined_assignments = ",".join([to_string(a) for a in assignments])
        return f'insert into atomic.{table_name}({joined_values}) values({joined_assignments})'

    def __str__(self):
        return f'Context({self.schema_vendor, self.schema_name, self.schema_format, self.schema_version})'


class Event:

    def __init__(self, event):
        self.event = event
        self.context_fields, self.simple_fields = partition(is_context_field, list(event.keys()))
        print(self.simple_fields)
        print(self.context_fields)

    def insert_stmts(self):

        event_id = self.event['event_id']
        collector_tstamp = self.event['collector_tstamp']

        stmts = [self._insert_stmt()]
        for context in self.context_fields:
            context = Context.create(context, self.event[context], event_id, collector_tstamp)
            if context:
                try:
                    stmts += context.insert_stmts()
                except Exception as ex:
                    logger.error(f'Exception during creation of insert stmt for {context}', ex)

        return stmts

    def _insert_stmt(self):
        values = ",".join(self.simple_fields)
        assignments = ",".join([to_string(self.event[key]) for key in self.simple_fields])
        return f'insert into atomic.events({values}) values({assignments})'


class PostgresLoader:

    def __init__(self, data_source_name):
        self.conn = psycopg2.connect(data_source_name)

    def insert_event(self, event):
        e = Event(event)
        insert_stmts = e.insert_stmts()
        cur = self.conn.cursor()
        for insert_stmt in insert_stmts:
            logger.debug(insert_stmt)
            cur.execute(insert_stmt)
        self.conn.commit()
