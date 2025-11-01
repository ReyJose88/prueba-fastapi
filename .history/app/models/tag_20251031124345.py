from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin, SoftDeleteMixin

class Tag(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    posts = relationship("Post", secondary="post_tags", back_populates="tags")