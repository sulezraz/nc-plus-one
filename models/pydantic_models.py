from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    user_password: str

class UserUpdate(BaseModel):
    username: str
    email: str
    user_password: str