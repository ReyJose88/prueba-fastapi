from typing import TypeVar, Generic, Type, Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.core.exceptions import DatabaseReadError
from datetime import datetime

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: AsyncSession):
        self.model = model
        self.session = session

    async def get_active(self, id: int) -> Optional[T]:
        try:
            query = select(self.model).where(
                self.model.id == id,
                self.model.deleted_at.is_(False)
            )
            result = await self.session.execute(query)
            return result.scalars().first()
        except SQLAlchemyError as e:
            raise DatabaseReadError(f"DB error fetching {self.model.__name__} {id}") from e

    async def list_active(self, skip: int = 0, limit: int = 20) -> List[T]:
        query = select(self.model).where(
            self.model.deleted_at.is_(False)
        ).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def soft_delete(self, id: int) -> bool:
        obj = await self.get_active(id)
        if not obj:
            return False
        obj.is_deleted = True
        obj.deleted_at = datetime.utcnow()
        await self.session.commit()
        return True