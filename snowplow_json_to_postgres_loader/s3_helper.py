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
    file = tempfile.NamedTemporaryFile()
    with open(file.name, 'wb') as f:
        s3.download_fileobj(bucket, key, f)
    with open(file.name) as f:
        lines = f.readlines()
    return lines
