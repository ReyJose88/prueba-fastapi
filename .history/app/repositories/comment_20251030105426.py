from app.models.comment import Comment
from .base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession

class CommentRepository(BaseRepository[Comment]):
    def __init__(self, session: AsyncSession):
        super().__init__(Comment, session)