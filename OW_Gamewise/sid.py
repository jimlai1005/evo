from __future__ import print_function
import re
import json
import uuid
from datetime import datetime
import time
import boto3

def put_session(sessionID, sessionUserId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('session')
    now = time.time()
    timestamp = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
    response = table.put_item(
       Item={
            'sid': sessionID,
            'userId': sessionUserId,
            'debitList': "",
            'createTime': timestamp
        }
    )
    #return response

def lambda_handler(event, context):
    try:
        qsParam = event['queryStringParameters']['authToken']
        if not (qsParam == "s3cr3tV4lu3"):
            context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'INVALID_TOKEN_ID'}),
                "isBase64Encoded": False
            }
            return context
    except:
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'INVALID_TOKEN_ID'}),
                "isBase64Encoded": False
            }
        return context

    try:
        bodyParam = event['body']
        bodyKeyId = json.loads(bodyParam)['userId']
        bodyKeyChannel = json.loads(bodyParam)['channel']
        bodyKeyType = bodyKeyChannel['type']
        bodyKeyUuid = json.loads(bodyParam)['uuid']

    except:
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'INVALID_PARAMETER'}),
                "isBase64Encoded": False
            }
        return context

    sid = uuid.uuid4().hex
    put_session(sid,bodyKeyId)

    responseBody = {
        'status': 'OK',
        'sid': sid,
        'uuid': bodyKeyUuid
    }

    context = {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": json.dumps(responseBody),
        "isBase64Encoded": False
    }
    return context
