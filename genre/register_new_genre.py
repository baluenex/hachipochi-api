# -*- coding: utf-8 -*-

import json
import time
from datetime import datetime, timezone
import boto3
import base64
from boto3.dynamodb.conditions import Key, Attr

now = time.time()
utc = datetime.fromtimestamp(now, timezone.utc)

s3 = boto3.resource('s3')
backet = "hachipochi-history"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hachipochi-table')

def lambda_handler(event, context):
    #print(event)
    genreData = json.loads(event["Records"][0]["body"])
    item_id = "genre_" + genreData[0]["cont_name"]
    register_time = str(utc)

    itemToS3 = {
        "item_id":item_id,
        "cont_name":"genre",
        "item_info":genreData,
        "register_time":register_time
    }
    key = item_id + ".json"
    object = s3.Object(backet, key)
    object.put(Body=json.dumps(itemToS3))

    item_info = json.dumps(genreData, ensure_ascii=False)
    itemToDynamo = {
        "item_id":item_id,
        "cont_name":"genre",
        "item_info":item_info,
        "register_time":register_time
    }
    table.put_item(
        Item=itemToDynamo
    )

    return True

if __name__ == "__main__":
    event = {
	   "Records": [
	      {
		     "body": "[{\"cont_name\": \"pachira\"},{\"value\": \"パキラ\"}]"
		  }
	   ]
    }
    context = {}
    lambda_handler(event, context)
