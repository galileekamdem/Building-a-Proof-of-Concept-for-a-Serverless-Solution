import boto3, json

client = boto3.client('sns')

def lambda_handler(event, context):

    for record in event["Records"]:

        if record['eventName'] == 'INSERT':
            new_record = record['dynamodb']['NewImage']    
            response = client.publish(
                TargetArn='arn:aws:sns:us-east-1:075617906240:POC-Topic',
                Message=json.dumps({'default': json.dumps(new_record)}),
                MessageStructure='json'
            )