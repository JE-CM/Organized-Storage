from pydantic import BaseModel

class UserData(BaseModel):
    name: str
    password: str

class UserId(UserData):
    id: int