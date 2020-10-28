import os

import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "snowplow_json_to_postgres_loader"))

import s3_helper


def test_read_json():
    lines = s3_helper.read_json_file(bucket='petersiemen-snowplow-tracking',
                                     key='2020/10/28/08/good-stream-enriched-converted-2-2020-10-28-08-52-28-6719202e-ec7a-406d-8042-ef1865268e99')

    for line in lines:
        print(line)
