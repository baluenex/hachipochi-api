import json
import boto3
import base64
from boto3.dynamodb.conditions import Key, Attr

sqs = boto3.resource('sqs')
queueName = 'HachipochiPostGenreQueue'
queue = sqs.get_queue_by_name(QueueName=queueName)

def lambda_handler(event, context):
    print(event)
    genreData = event['body']
    message = [{"Id" : "genre" , "MessageBody" : genreData}]
    response = queue.send_messages(Entries=message)
    items = {'result': 'success'}
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(items)
    }

if __name__ == "__main__":
    event = {"body": '''[{"cont_name": "pachira"},{"value": "パキラ"}]'''}
    context = {}
    lambda_handler(event, context)
