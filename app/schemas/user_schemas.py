from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    account: EmailStr
    password: str

class UserCreateResponse(BaseModel):
    user_ID: int
    account: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
