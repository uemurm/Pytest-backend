from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(
        min_length=1, max_length=100,
        description="User's full name (1-100 characters)"
    )
    email: EmailStr  # A Pydantic class for Email validation
    age: int = Field(ge=0, le=150,  # 0 <= age <= 150
                     description="User's age (must be between 0 and 150)")


class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    age: Optional[int] = Field(default=None,
                               # Same rule applies as creating
                               ge=0, le=150)


class User(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
