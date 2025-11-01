from pydantic import BaseModel, Field
from datetime import datetime
from .user import UserRead
from typing import Optional

class CommentBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000)

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int
    user: UserRead
    post_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    is_deleted: Optional[bool] = None
    deleted_at: Optional[datetime] = None

    model_config = {"from_attributes": True}