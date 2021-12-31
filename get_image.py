import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('hachipochi-table')

def lambda_handler(event, context):
    cont_name = event['queryStringParameters']['cont_name']
    print(cont_name)

    result = table.query(
        IndexName = 'cont_name-index',
        KeyConditionExpression = Key('cont_name').eq(cont_name),
        ScanIndexForward = False
    )

    items = result['Items']
    print(items)
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(items)
    }

if __name__ == "__main__":
    event = {
        'queryStringParameters' : {
            'cont_name' : 'hachipochi'
        }
    }
    context = {}
    lambda_handler(event, context)
