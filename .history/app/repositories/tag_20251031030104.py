from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.tag import Tag
from .base import BaseRepository

class TagRepository(BaseRepository[Tag]):
    def __init__(self, session: AsyncSession):
        super().__init__(Tag, session)

    async def get_by_name(self, name: str) -> Tag | None:
        result = await self.session.execute(select(Tag).where(Tag.name == name, Tag.deleted.is_(False)))
        return result.scalars().first()