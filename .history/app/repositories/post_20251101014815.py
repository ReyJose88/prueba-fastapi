from app.models.post import Post
from .base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from typing import Optional
from app.models.post import Post
from sqlalchemy import select

class PostRepository(BaseRepository[Post]):
    def __init__(self, session: AsyncSession):
        super().__init__(Post, session)
        

    async def get_active_with_relations(self, id: int) -> Optional[Post]:
        query = (
            select(Post)
            .options(
                selectinload(Post.tags),
                selectinload(Post.comments)
            )
            .where(Post.id == id, Post.is_deleted.is_(False))
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def list_active_with_relations(self, skip: int = 0, limit: int = 20):
        query = (
            select(Post)
            .options(
                selectinload(Post.tags),
                selectinload(Post.comments)
            )
            .where(Post.is_deleted.is_(False))
            .offset(skip)
            .limit(limit)
        )
        result = await self.session.execute(query)
        return result.scalars().all()