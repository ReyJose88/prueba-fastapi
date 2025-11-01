from app.models.post import Post
from .base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession

class PostRepository(BaseRepository[Post]):
    def __init__(self, session: AsyncSession):
        super().__init__(Post, session)