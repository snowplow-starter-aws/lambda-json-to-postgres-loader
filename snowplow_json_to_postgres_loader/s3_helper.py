import boto3
import tempfile
import os
import botocore
from botocore.config import Config

if os.getenv('IN_VPC'):
    region = os.getenv('AWS_REGION')
    s3 = boto3.client('s3', region, config=Config(s3={'addressing_style': 'path'}))
else:
    s3 = boto3.client('s3')


def with_temp_file():
    with tempfile.TemporaryFile(mode='wb') as f:
        yield f


def read_json_file(bucket, key):
    #  the file is deleted on close
    with tempfile.NamedTemporaryFile(mode='wb') as f:
        s3.download_fileobj(bucket, key, f)
        f.flush()
        with open(f.name) as r:
            lines = r.readlines()
    return lines
