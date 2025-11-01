from sqlalchemy import String, Integer, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin, SoftDeleteMixin

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)

class Post(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    #author = relationship("User", back_populates="posts")
    #comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    #tags = relationship("Tag", secondary=post_tags, back_populates="posts")