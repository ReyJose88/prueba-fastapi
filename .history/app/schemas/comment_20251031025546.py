from pydantic import BaseModel, Field
from datetime import datetime
from .user import UserRead

class CommentBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000)

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int
    user: UserRead
    post_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}