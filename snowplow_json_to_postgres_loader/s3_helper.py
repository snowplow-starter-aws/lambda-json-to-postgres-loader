import boto3
import tempfile

s3 = boto3.client('s3')


def with_temp_file():
    with tempfile.TemporaryFile(mode='wb') as f:
        yield f


def read_json_file(bucket, key):
    file = tempfile.NamedTemporaryFile()
    with open(file.name, 'wb') as f:
        s3.download_fileobj(bucket, key, f)

    with open(file.name) as f:
        return f.readlines()
