import json
import boto3
import os


def scan(event, context):
    dynamoDB = boto3.resource('dynamodb')
    table = dynamoDB.Table(f'{os.environ["ENV"]}-hachipochi-genre')
    result = table.scan()
    items = result['Items']

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(items)
    }

if __name__ == "__main__":
    os.environ["ENV"] = "dev"
    event = {}
    context = {}
    scan(event, context)
