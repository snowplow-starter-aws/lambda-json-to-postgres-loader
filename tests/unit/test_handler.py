import sys
import os
import psycopg2
from testcontainers.postgres import PostgresContainer
from .database_helper import migrated_testcontainer

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "snowplow_json_to_postgres_loader"))

import pytest

import app


@pytest.fixture()
def s3_event():
    """ Generates API GW Event"""

    return {
        "Records": [
            {
                "eventVersion": "2.0",
                "eventSource": "aws:s3",
                "awsRegion": "us-east-1",
                "eventTime": "1970-01-01T00:00:00.000Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {
                    "principalId": "EXAMPLE"
                },
                "requestParameters": {
                    "sourceIPAddress": "127.0.0.1"
                },
                "responseElements": {
                    "x-amz-request-id": "EXAMPLE123456789",
                    "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "testConfigRule",
                    "bucket": {
                        "name": "petersiemen-snowplow-tracking",
                        "ownerIdentity": {
                            "principalId": "EXAMPLE"
                        },
                        "arn": "arn:aws:s3:::petersiemen-snowplow-tracking"
                    },
                    "object": {
                        "key": "2020/10/28/08/good-stream-enriched-converted-2-2020-10-28-08-52-28-6719202e-ec7a-406d-8042-ef1865268e99",
                        "size": 1024,
                        "eTag": "0123456789abcdef0123456789abcdef",
                        "sequencer": "0A1B2C3D4E5F678901"
                    }
                }
            }
        ]
    }


def test_lambda_handler(s3_event):
    with migrated_testcontainer() as dsn:
        ret = app.lambda_handler(s3_event, "")
        print(ret)
        assert ret["statusCode"] == 200
