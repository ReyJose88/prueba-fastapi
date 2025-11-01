from pydantic import BaseModel, EmailStr, Field

class Comment(BaseModel):
    id: int
    content: str = Field(..., min_length=1, max_length=500)
    author_id: int
    post_id: int