from exceptions.validation_exception import ValidationException


class UserService:

    def __init__(self, repo):
        self.repo = repo

    def create_user(self, user):
        self.__validate_age(user.age)

        result = self.repo.save(user)

        return {
            "message": "User created successfully",
            "data": result
        }

    def __validate_age(self, age):
        if age < 18:
            raise ValidationException("Age must be 18+")