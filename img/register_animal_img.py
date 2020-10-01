import json
import time
from datetime import datetime, timezone, timedelta
import boto3
import base64
from boto3.dynamodb.conditions import Key, Attr

s3 = boto3.resource('s3')
bucket = s3.Bucket('hachipochi-history')
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('hachipochi-table')

def lambda_handler(event, context):
    print(event)
    now = time.time()
    utc = datetime.fromtimestamp(now, timezone.utc)
    print(utc)
    #imgData = event['Records'][0]
    #s3にhistorを追加
    #Key = 'hachippochi-img/'+ imagePath['name']
    #bucket.put_object(
    #    Body = imageData,
    #    Key = Key
    #)
    #DynamoDBに画像情報を追加
    #table.put_item(
    #    Item = {
    #        'img_title': imgData['title'],
    #        'cont_name': imgData['cont_name'],
    #        'img_name': imgData['img_name']
    #        'register_time':utc
    #    }
    #)

if __name__ == "__main__":
    event = {}
    context = {}
    lambda_handler(event, context)
