from __future__ import print_function
import re
import json
import uuid
from decimal import Decimal
import boto3
from decimal import Decimal 
from datetime import datetime
import time

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

def update_transaction(transactionID, transactionAmount, transactionType, transactionIsDelete, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    response = table.update_item(
        Key={
            'transaction.id': transactionID,
        },
        UpdateExpression="set amount=:r, type=:p, isdelete=:a",
        ExpressionAttributeValues={
            ':r': transactionAmount,
            ':p': transactionType,
            ':a': transactionIsDelete
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

def get_isdelete(transactionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    try:
        response = table.get_item(Key={'transaction.id': transactionID})
        res = response['Item']['transaction.id']
    except:
        return 2 # no such debit transaction
    else:
        return response['Item']['isdelete']

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
    #return response

def verify_transaction(transactionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    try:
        response = table.get_item(Key={'transaction.id': transactionID})
    except:
        return 0
    else:
        return 1

def verify_creditTransaction(transactionRefId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    try:
        response = table.get_item(Key={'refId': transactionRefId})
    except:
        return 2
    else:
        for items in response:
            if (items['Item']['type'] == 'credit') or (items['Item']['type'] == 'cancel'):
                return 1
    return 0

def get_isdelete(transactionID, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    try:
        response = table.get_item(Key={'transaction.id': transactionID})
        res = response['Item']['transaction.id']
        try:
            return response['Item']['isdelete']
        except:
            return 0
    except:
        return 2 # no such debit transaction

# for credit!
def get_isdelete(transactionID, transactionGId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    try:
        # response = table.get_item(Key={'transaction.id': transactionID})
        response = table.get_item(Key={'transaction.id': 'D' + transactionID[1:]})
        res = response['Item']['transaction.id']
        if transactionGId == response['Item']['gameId']:
            return response['Item']['isdelete']
        else:
            return 0
    except:
        return 2 # no such debit transaction

        


from datetime import datetime
import time
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
            'createTime': timestamp
        }
    )
    return response

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

