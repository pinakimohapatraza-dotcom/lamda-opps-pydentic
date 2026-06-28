import boto3
import os
import json

class SQSService:
    def __init__(self):
        self.client = boto3.client("sqs")
        self.queue_url = os.environ["QUEUE_URL"]

    
    def send_message(self, payload):
        return self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(payload)
        )