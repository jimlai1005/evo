from __future__ import print_function
import re
import json
import boto3
from decimal import Decimal 
from datetime import datetime
import time

def update_debit(sessionID, transactionRefID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('session')
    try:
        response = table.get_item(Key={'sid': sessionID})
        debitList = response['Item']['debitList']
    except:
        debitList = ""
        print('Get debitList failed!')
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'Get DebitList Failed!'}),
                "isBase64Encoded": False
            }
        return context

    response = table.update_item(
        Key={'sid': sessionID},
        UpdateExpression="set debitList = :list",
        ExpressionAttributeValues={
            ':list': transactionRefID + "," + debitList
        },
        ReturnValues="UPDATED_NEW"
    )
    #return response

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

def verify_transaction(transactionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    try:
        response = table.get_item(Key={'transaction.id': transactionID})
        res = response['Item']['transaction.id']
    except:
        return 0
    else:
        return 1

def put_transaction(transactionID, transactionGId, transactionAmount, transactionType, transactionIsDelete, transactionUserId, transactionRefId,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    now = time.time()
    timestamp = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = table.put_item(
           Item={
                'transaction.id': transactionID,
                'gameId': transactionGId,
                'amount': transactionAmount,
                'type': transactionType,
                'isdelete': transactionIsDelete,
                'userId': transactionUserId,
                'refId': transactionRefId,
                'createTime': timestamp,
                'updateTime': ""
            }
        )
    except:
        print('Put failed!')
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'Put Failed!'}),
                "isBase64Encoded": False
            }
        return context

    #return response

def add_balance(userId, addAmount, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user')
    try:
        response = table.update_item(
            Key={
                'userId': userId,
            },
            UpdateExpression="set balance = balance + :val",
            ExpressionAttributeValues={
                ':val': addAmount
            },
            ReturnValues="UPDATED_NEW"
        )
    except:
        print('Add failed!')
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'Add Failed!'}),
                "isBase64Encoded": False
            }
        return context
    #return response
    
def get_balance(userId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user')
    try:
        response = table.get_item(Key={'userId': userId})
        return response['Item']['balance']
    except:
        print(e.response['Error']['Message'])
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'Get Balance Failed!'}),
                "isBase64Encoded": False
            }
        return 0
        
        
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
        bodyKeyGame = json.loads(bodyParam)['game']
        bodyKeyGid = bodyKeyGame['id']
        bodyKeyTransaction = json.loads(bodyParam)['transaction']
        bodyKeyTid = bodyKeyTransaction['id']
        bodyKeyTrefId = bodyKeyTransaction['refId']
        bodyKeyTamount = bodyKeyTransaction['amount']    
        bodyKeyCcy = json.loads(bodyParam)['currency']
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

    if float(get_balance(bodyKeyId)) - bodyKeyTamount <0:
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'INSUFFICIENT_FUNDS'}),
                "isBase64Encoded": False
            }
        return context

    if verify_transaction(bodyKeyTid) == 1: # debit transaction exists
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'BET_ALREADY_EXIST'}),
                "isBase64Encoded": False
            }
        return context

    put_transaction(bodyKeyTid, bodyKeyGid, Decimal(str(bodyKeyTamount)), "debit" , 0, bodyKeyId, bodyKeyTrefId)
    
    add_balance(bodyKeyId, Decimal(str(bodyKeyTamount)) * (-1))

    update_debit(bodyKeySid, bodyKeyTrefId)

    responseBody = {
        'status': 'OK',
        'balance': float(get_balance(bodyKeyId)),
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
