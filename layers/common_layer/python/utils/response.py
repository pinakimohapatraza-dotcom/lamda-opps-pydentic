

class Response:

    def success(self, data):

        return {
            "statusCode": 200,
            "bode" : data
        }

    def error(self, msg):
        return {
            "statusCode" : 500,
            "body": msg

        }