from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TagRead(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}