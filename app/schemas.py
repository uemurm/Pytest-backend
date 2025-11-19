from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr  # A Pydantic class for Email validation
    age: int = Field(ge=0, le=150)  # 0 <= age <= 150


class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=0, le=150)  # Same rule applies when updating


class User(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
