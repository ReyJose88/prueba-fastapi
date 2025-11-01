from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from .user import UserRead
from .comment import CommentRead
from .tag import TagRead

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=10, max_length=500)

class PostCreate(PostBase):
    tags: Optional[List[str]] = []

class PostRead(PostBase):
    id: int
    user: UserRead
    comments: Optional[List[CommentRead]] = []
    tags: Optional[List[TagRead]] = []
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}