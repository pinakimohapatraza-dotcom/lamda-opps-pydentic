from exceptions.validation_exception import ValidationException



class UserService:

    def __init__(self, repo, sqs):
        self.repo = repo
        self.sqsclient=  sqs

    def create_user(self, user):
        self.__validate_age(user.age)

        result = self.repo.save(user)
        self.sqsclient.send_message(user.model_dump())

        return {
            "message": "User created successfully",
            "data": result
        }

    def __validate_age(self, age):
        if age < 18:
            raise ValidationException("Age must be 18+")