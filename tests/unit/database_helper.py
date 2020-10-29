import os
from testcontainers.postgres import PostgresContainer
import psycopg2
from contextlib import contextmanager


def get_migration_files():
    path = os.path.join(os.path.dirname(__file__), os.pardir, "migration")
    files = os.listdir(path)
    files.sort()
    for f in files:
        yield os.path.join(path, f)


def migrate(conn):
    cur = conn.cursor()
    for f in get_migration_files():
        with open(f) as fp:
            stmt = " ".join(fp.readlines())
            cur.execute(stmt)
            conn.commit()


@contextmanager
def migrated_testcontainer():
    with PostgresContainer("postgres:13.0") as postgres:
        os.environ["DATABASE"] = 'test'
        os.environ["HOST"] = postgres.get_container_host_ip()
        os.environ["PORT"] = postgres.get_exposed_port(5432)
        os.environ["USERNAME"] = postgres.POSTGRES_USER
        os.environ["PASSWORD"] = postgres.POSTGRES_PASSWORD
        dsn = f"dbname='test' host='{postgres.get_container_host_ip()}' port='{postgres.get_exposed_port(5432)}' user='{postgres.POSTGRES_USER}' password='{postgres.POSTGRES_PASSWORD}'"
        conn = psycopg2.connect(dsn)

        migrate(conn)
        yield dsn
