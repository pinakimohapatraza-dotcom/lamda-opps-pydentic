from utils.response import Response
from models.user_model import UserModel
from services.user_service import UserService
from repositories.user_repository import UserRepository
from exceptions.validation_exception import ValidationException


resp = Response()


def lambda_handler(event, context):

    try:
        print(context.aws_request_id)
        print(context.get_remaining_time_in_millis())
        user = UserModel(**event)

        repo = UserRepository()

        service = UserService(repo)

        result = service.create_user(user)

        return resp.success(result)

    except ValidationException as e:
        return resp.error(str(e))

    except Exception as e:
        return resp.error(str(e))

