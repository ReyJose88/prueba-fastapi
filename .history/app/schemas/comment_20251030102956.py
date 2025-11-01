from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=10, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)