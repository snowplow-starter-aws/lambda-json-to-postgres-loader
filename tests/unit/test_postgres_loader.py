import json

import pytest
from testcontainers.postgres import PostgresContainer
import psycopg2

from snowplow_json_to_postgres_loader import postgres_loader


@pytest.fixture()
def database_container():
    with PostgresContainer("postgres:9.5") as postgres:
        print(postgres.get_connection_url())
        conn = psycopg2.connect(
            f"host='{postgres.get_container_host_ip()}' port='{postgres.get_exposed_port(5432)}' user='{postgres.POSTGRES_USER}' password='{postgres.POSTGRES_PASSWORD}'")
        cur = conn.cursor()
        cur.execute('select 1;')
        conn.commit()


@pytest.fixture()
def single_event():
    """ Generates API GW Event"""

    return {
        "app_id": "homepage",
        "platform": "web",
        "etl_tstamp": "2020-10-27T16:50:47.000Z",
        "collector_tstamp": "2020-10-27T16:50:42.806Z",
        "dvce_created_tstamp": "2020-10-27T16:50:42.686Z",
        "event": "page_view",
        "event_id": "08ade0a5-2b97-40d5-ae82-0cde93694790",
        "name_tracker": "snowplow",
        "v_tracker": "js-2.16.2",
        "v_collector": "ssc-1.0.1-kinesis",
        "v_etl": "stream-enrich-1.1.3-common-1.1.3",
        "user_ipaddress": "172.17.0.1",
        "domain_userid": "f7af14d6-df15-4721-b5e8-a99de86dce84",
        "domain_sessionidx": 1,
        "network_userid": "ff27c2bc-3436-4c94-8738-829b67d12cf8",
        "page_url": "http://localhost:8000/cross-account-multi-region-ci-cd-pipeline-on-aws",
        "page_urlscheme": "http",
        "page_urlhost": "localhost",
        "page_urlport": 8000,
        "page_urlpath": "/cross-account-multi-region-ci-cd-pipeline-on-aws",
        "contexts__com_snowplowanalytics_snowplow__web_page__1": [
            {
                "id": "a62e7007-0054-4c9b-98bc-1d7820da71ca"
            }
        ],
        "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "br_lang": "en-US",
        "br_features_pdf": True,
        "br_features_flash": False,
        "br_features_java": False,
        "br_features_director": False,
        "br_features_quicktime": False,
        "br_features_realplayer": False,
        "br_features_windowsmedia": False,
        "br_features_gears": False,
        "br_features_silverlight": False,
        "br_cookies": True,
        "br_colordepth": "24",
        "br_viewwidth": 1528,
        "br_viewheight": 870,
        "os_timezone": "Europe/Berlin",
        "dvce_screenwidth": 1920,
        "dvce_screenheight": 1080,
        "doc_charset": "UTF-8",
        "doc_width": 1513,
        "doc_height": 3841,
        "dvce_sent_tstamp": "2020-10-27T16:50:42.715Z",
        "contexts__com_snowplowanalytics_snowplow__ua_parser_context__1": [
            {
                "useragentFamily": "Chrome",
                "useragentMajor": "86",
                "useragentMinor": "0",
                "useragentPatch": "4240",
                "useragentVersion": "Chrome 86.0.4240",
                "osFamily": "Linux",
                "osMajor": None,
                "osMinor": None,
                "osPatch": None,
                "osPatchMinor": None,
                "osVersion": "Linux",
                "deviceFamily": "Other"
            }
        ],
        "domain_sessionid": "d8116ac3-9280-4253-a272-473f6e16348b",
        "derived_tstamp": "2020-10-27T16:50:42.777Z",
        "event_vendor": "com.snowplowanalytics.snowplow",
        "event_name": "page_view",
        "event_format": "jsonschema",
        "event_version": "1-0-0"
    }


# def test_postgres_loader(single_event):
#     loader = postgres_loader.PostgresLoader()
#     i = loader.insert_event(single_event)

# assert "location" in data.dict_keys()


#
# def test_ua_parser_context(single_event):
#     print(single_event)
#     name = 'contexts__com_snowplowanalytics_snowplow__ua_parser_context__1'
#     context = postgres_loader.Context.create(name=name, objs=single_event[name], event_id='234', collector_tstamp='4563')
#
#     print(context)
#     print(context.insert_stmts())
#
# def test_web_page(single_event):
#     print(single_event)
#     name = 'contexts__com_snowplowanalytics_snowplow__web_page__1'
#     context = postgres_loader.Context.create(name=name, objs=single_event[name], event_id='234', collector_tstamp='4563')
#
#     print(context)
#     print(context.insert_stmts())
#
#
# def test_process_event(single_event):
#     print(single_event)
#     postgres_loader.Event(single_event)


def test_testcontainer(database_container):
    print(1)
