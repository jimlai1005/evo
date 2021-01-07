from __future__ import print_function
import re
import json
import uuid
from decimal import Decimal
import boto3
from decimal import Decimal 
from datetime import datetime
import time

def put_transaction(transactionID, transactionAmount, transactionType, transactionIsDelete, transactionUserId, transactionRefId,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transaction')
    now = time.time()
    timestamp = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
    response = table.put_item(
       Item={
            'transaction.id': transactionID,
            'amount': transactionAmount,
            'type': transactionType,
            'isdelete': transactionIsDelete,
            'userId': transactionUserId,
            'refId': transactionRefId,
            'createTime': timestamp
        }
    )
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
    #return response
    
def get_balance(userId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user')
    try:
        response = table.get_item(Key={'userId': userId})
    except:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['balance']

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
    except:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['isdelete']


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

