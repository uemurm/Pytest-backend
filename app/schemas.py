from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr  # A class for Email validation
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

class User(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
