import json
from urllib.parse import unquote_plus
import s3_helper
import os
import logging
from postgres_loader import PostgresLoader

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('Loading function')


def lambda_handler(event, context):
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    dsn = f"host='{HOST}' port='{PORT}' user='{USERNAME}' password='{PASSWORD}'"

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])
    print(key)

    lines = s3_helper.read_json_file(bucket, key)
    loader = PostgresLoader(dsn)

    success = 0
    failure = 0
    for line in lines:
        single_event = json.loads(line)
        try:
            loader.insert_event(single_event)
            success += 1
        except:
            logger.error(f'exception during processing of {line}')
            failure += 1

    status_code = 500
    if success > failure:
        status_code = 200
    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": f"Processes {success} events successfully. {failure} failures."
        }),
    }
