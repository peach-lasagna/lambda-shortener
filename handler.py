from crud import DataBase
import boto3
from typing import Dict, Optional
from boto3.dynamodb.conditions import Key
from short import encode_url

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
db = DataBase(dynamodb, "Urls")
get_val = lambda st, e: db.table.query(KeyConditionExpression=Key(st).eq(e[st.lower()]))['Items']

def read_handler(event: Dict[str, str], context):
    """
    event  ~ {reduction: test}
    """
    return db.read(event["reduction"])

def write_handler(event: Dict[str, Optional[str]], context):
    """
    event ~ { reduction: test ,  url: test.com}
    """

    if event["reduction"] and not get_val("Reduction", event):
        resp = event["reduction"]
        db.create(resp, event['url'])
        return resp
    short = get_val("URL", event)
    if short:
        return short
    response = db.client.describe_table(TableName='Urls')
    uid = response['Table']['ItemCount']
    reduct = encode_url(uid)
    db.create(reduct, event['url'])
    return {"Reduction": reduct}
