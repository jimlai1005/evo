from __future__ import print_function
import re
import json
import boto3

def verify_session(sessionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('session')
    try:
        response = table.get_item(Key={'sid': sessionID})
        res = response['Item']['sid']
    except:
        return 0
    else:
        return 1

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
        bodyKeyChannel = json.loads(bodyParam)['channel']
        bodyKeyType = bodyKeyChannel['type']
        bodyKeyUuid = json.loads(bodyParam)['uuid']

        try:
            bodyKeySid = json.loads(bodyParam)['sid']
            if not (bodyKeySid == "111ssss3333rrrrr45555" or bodyKeySid == "111ssss3333rrrrr46666" or verify_session(bodyKeySid)):
                context = {
                    "statusCode": 200,
                    "headers": {
                        "my_header": "my_value"
                    },
                    "body": json.dumps({'status': 'INVALID_SID'}),
                    "isBase64Encoded": False
                }
                return context
        except:
            context = {
                    "statusCode": 200,
                    "headers": {
                        "my_header": "my_value"
                    },
                    "body": json.dumps({'status': 'INVALID_SID'}),
                    "isBase64Encoded": False
                }
            return context

        try:
            bodyKeyId = json.loads(bodyParam)['userId']
            if not (bodyKeyId == "a1a2a3a4" or bodyKeyId == "b1b2b3b4"):
                context = {
                    "statusCode": 200,
                    "headers": {
                        "my_header": "my_value"
                    },
                    "body": json.dumps({'status': 'INVALID_PARAMETER'}),
                    "isBase64Encoded": False
                }
                return context
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

    responseBody = {
        'status': 'OK',
        'sid': bodyKeySid,
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
