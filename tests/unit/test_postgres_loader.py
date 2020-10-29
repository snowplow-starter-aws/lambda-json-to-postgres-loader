import os
import sys
import pytest
from testcontainers.postgres import PostgresContainer
from .database_helper import migrate
from .database_helper import migrated_testcontainer

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "snowplow_json_to_postgres_loader"))

from postgres_loader import *


@pytest.fixture()
def another_event():
    return {
        "app_id": "homepage",
        "platform": "web",
        "etl_tstamp": "2020-10-29T15:42:33.856Z",
        "collector_tstamp": "2020-10-29T15:42:24.696Z",
        "dvce_created_tstamp": "2020-10-29T15:42:24.659Z",
        "event": "page_view",
        "event_id": "af48862e-8e27-4a3d-aa7a-5be71a46e181",
        "name_tracker": "snowplow",
        "v_tracker": "js-2.16.2",
        "v_collector": "ssc-1.0.1-kinesis",
        "v_etl": "stream-enrich-1.1.3-common-1.1.3",
        "user_ipaddress": "91.65.137.70",
        "domain_userid": "becb6cfb-4681-4480-a7cb-d8e001ae53ae",
        "domain_sessionidx": 5,
        "network_userid": "00000000-0000-4000-a000-000000000000",
        "page_url": "https://www.petersiemen.net/availability-and-durability-for-plants",
        "page_urlscheme": "https",
        "page_urlhost": "www.petersiemen.net",
        "page_urlport": 443,
        "page_urlpath": "/availability-and-durability-for-plants",
        "contexts__com_snowplowanalytics_snowplow__web_page__1": [{"id": "acf326ac-460e-43b5-91a8-3bfd982861e4"}],
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
        "br_viewheight": 490,
        "os_timezone": "Europe/Berlin",
        "dvce_screenwidth": 1920,
        "dvce_screenheight": 1080, "doc_charset": "UTF-8",
        "doc_width": 1513,
        "doc_height": 3152,
        "dvce_sent_tstamp": "2020-10-29T15:42:24.664Z",
        "contexts__com_snowplowanalytics_snowplow__ua_parser_context__1": [
            {"useragentFamily": "Chrome",
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
             "deviceFamily": "Other"}],
        "contexts__org_ietf__http_cookie__1": [
            {"name": "sp",
             "value": "00000000-0000-4000-A000-000000000000"}
        ],
        "domain_sessionid": "5d2b9d35-2754-42c6-bacb-adc681d7b792",
        "derived_tstamp": "2020-10-29T15:42:24.691Z",
        "event_vendor": "com.snowplowanalytics.snowplow",
        "event_name": "page_view",
        "event_format": "jsonschema",
        "event_version": "1-0-0",
        "event_fingerprint": "9bc42207de47c08bd05e8691c7abf8cc"}


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


# def test_testcontainer(single_event):
#     with migrated_testcontainer() as dsn:
#         loader = PostgresLoader(dsn)
#         i = loader.insert_event(single_event)


def test_insert_another(another_event):
    with migrated_testcontainer() as dsn:
        loader = PostgresLoader(dsn)
        i = loader.insert_event(another_event)

# def test_list():
#     get_migration_files()
