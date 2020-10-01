import json
import boto3
import base64
from boto3.dynamodb.conditions import Key, Attr

s3 = boto3.resource('s3')
bucket = s3.Bucket('hachipochi-img')
sqs = boto3.resource('sqs')
queueName = 'HachipochiPostImgQueue'
queue = sqs.get_queue_by_name(QueueName=queueName)

def lambda_handler(event, context):
    print(event)
    #バイナリがBase64にエンコードされているので、ここでデコード
    imageBody = base64.b64decode(event['body']['file'])
    print(imageBody)
    #画像保存先の設定
    imageName = event['params']['path']['name']
    Key = 'hachipochi-img/'+ imageName
    print(Key)
    #bucket.put_object(
    #    Body = imageBody,
    #    Key = Key
    #)
    print('S3 put Success!!')

    #画像情報をSQSに送信する
    imgData = {'title': event['body'][title], 'cont_name': event['body']['cont_name'], img_name: imageName}
    print(imgData)
    message = [{'Id':'test', 'MessageBody':imgData}]
    #response = queue.send_messages(Entries=message)
    print(response)
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
    event = {}
    context = {}
    lambda_handler(event, context)
