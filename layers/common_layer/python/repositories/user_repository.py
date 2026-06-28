class UserRepository:

    def save(self, user):
        print("Saving user to database/SQS")

        return {
            "id": 101,
            "name": user.name,
            "email": user.email,
            "age": user.age
        }