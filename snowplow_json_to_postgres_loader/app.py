import json
from urllib.parse import unquote_plus
import psycopg2
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])
    print(key)

    conn = psycopg2.connect("dbname='snowplow' host='172.17.0.1' user='postgres' password='postgres'")
    cur = conn.cursor()
    sqlInsertRow1 = "insert into atomic.events(collector_tstamp,event_id,v_collector,v_etl) values(now(),'aaa','aaa','aaa')"
    cur.execute(sqlInsertRow1)
    conn.commit()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
