from __future__ import print_function
import re
import json
import boto3
from decimal import Decimal 
from datetime import datetime
import time

def gamewise_cancel_transaction(sessionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    now = time.time()
    timestamp = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')

    try:    
        table = dynamodb.Table('session')
        response = table.get_item(Key={'sid': sessionID})

        debitList = response['Item']['debitList']
        RefIDList = debitList.split(",")
    except:
        RefIDList = ""
        print('Get debitList failed!')

    try:
        table = dynamodb.Table('transaction')
        for RefIDitem in RefIDList: 
            if not (RefIDitem == ""):
                response = table.update_item(
                    Key={
                        'transaction.id': 'D' + RefIDitem
                    },
                    UpdateExpression="set isdelete=:val, updateTime=:time",
                    ExpressionAttributeValues={
                        ':val': 1,
                        ':time': timestamp
                    },
                    ReturnValues="UPDATED_NEW"
                )
    except:
        print('Update transaction failed!')
    try:   
        table = dynamodb.Table('session')
        response = table.update_item(
            Key={'sid': sessionID},
            UpdateExpression="set debitList = :list",
            ExpressionAttributeValues={
                ':list': ''
            },
            ReturnValues="UPDATED_NEW"
        )
    except:
        print('Update session failed!')

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

def cancel_transaction(transactionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    now = time.time()
    timestamp = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = table.update_item(
            Key={
                'transaction.id': transactionID
            },
            UpdateExpression="set isdelete=:val, updateTime=:time",
            ExpressionAttributeValues={
                ':val': 1,
                ':time': timestamp
            },
            ReturnValues="UPDATED_NEW"
        )
    except:
        print('Cancel failed!')
    #return response

def clean_session(sessionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('session')
    try:
        response = table.update_item(
            Key={
                'sid': sessionID
            },
            UpdateExpression="set debitList=:list",
            ExpressionAttributeValues={
                ':list': ""
            },
            ReturnValues="UPDATED_NEW"
        )
    except:
        print('Clean failed!')

    #return response

def get_isdelete(transactionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    try:
        response = table.get_item(Key={'transaction.id': transactionID})
        res = response['Item']['transaction.id']
        try:
            if response['Item']['type'] =='cancel':
                return 1
            elif response['Item']['type'] =='debit':
                return 0
        except:
            return 0
    except:
        return 2 # no such debit transaction

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

    if verify_transaction(bodyKeyTid) == 0: # debit transaction exists
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'BET_DOES_NOT_EXIST'}),
                "isBase64Encoded": False
            }
        return context

    if get_isdelete(bodyKeyTid) == 1: # no settlement transaction
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'BET_ALREADY_SETTLED'}),
                "isBase64Encoded": False
            }
        return context
    elif get_isdelete(bodyKeyTid) == 2:
        context = {
                "statusCode": 200,
                "headers": {
                    "my_header": "my_value"
                },
                "body": json.dumps({'status': 'BET_DOES_NOT_EXIST'}),
                "isBase64Encoded": False
            }
        return context

    # gamewise_cancel_transaction(bodyKeySid)

    # cancel_transaction(bodyKeyTid)

    # clean_session(bodyKeySid)

    put_transaction(bodyKeyTid, bodyKeyGid, Decimal(str(bodyKeyTamount)), "cancel" , 1, bodyKeyId, bodyKeyTrefId)

    add_balance(bodyKeyId, Decimal(str(bodyKeyTamount)))

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
