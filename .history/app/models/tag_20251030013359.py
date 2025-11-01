from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin, SoftDeleteMixin

class Tag(Base, TimestampMixin, SoftDeleteMixin):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    posts = relationship("Post", secondary=post_tag, back_populates="tags")