import psycopg2

def is_not_context_field(element):
    return not element.startswith("contexts")


def to_string(value):
    if isinstance(value, int) or isinstance(value, float):
        return str(value)
    else:
        return f"'{value}'"


class PostgresLoader:

    def __init__(self):
        self.conn = psycopg2.connect("dbname='snowplow' host='172.17.0.1' user='postgres' password='postgres'")

    def insert_event(self, event):
        cur = self.conn.cursor()

        simple_fields = list(filter(is_not_context_field, event.keys()))
        values = ",".join(simple_fields)
        assignments = ",".join([to_string(event[key]) for key in simple_fields])
        insert = f'insert into atomic.events({values}) values({assignments})'
        cur.execute(insert)
        self.conn.commit()

        print(event)
        return insert
