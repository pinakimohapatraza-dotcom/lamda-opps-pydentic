from utils.response import Response
import json

resp = Response()


def lambda_handler(event, context):

    try:
        print(context.aws_request_id)
        for record in event["Records"]:
            

            body = json.loads(record["body"])

            order = {
                "user_id": body["user_id"],
                "item": body["item"]
            }

            print("Processing order:", order)
        

        return resp.success("Order processed successfully")

    

    except Exception as e:
        return resp.error(str(e))

