from pydantic  import BaseModel, Field, EmailStr 

class UserModel(BaseModel):
    name: str = Field(..., description="The name of the user")
    email: EmailStr = Field(..., description="The email of the user")
    age: int = Field(..., description="The age of the user")