from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
