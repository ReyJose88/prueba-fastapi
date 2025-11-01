from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=50)

class UserRead(UserBase):
    id: int
    created_at: datetime    
    updated_at: Optional[datetime] = None
    deleted: Optional[datetime] = None

    model_config = {"from_attributes": True}