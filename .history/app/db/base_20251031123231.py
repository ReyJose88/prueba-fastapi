from sqlalchemy import Column, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

class SoftDeleteMixin:
    deleted = Column(Boolean, default=False, nullable=False)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()