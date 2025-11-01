from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin, SoftDeleteMixin


class Tag(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False, index=True)

    posts = relationship(
        "Post", 
        secondary="post_tags",
        back_populates="tags",
        lazy="dynamic"
    )

    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"

    @property
    def post_count(self):
        return self.posts.count() if self.posts else 0

    @classmethod
    def find_or_create_by_name(cls, session, tag_name):
        existing_tag = session.query(cls).filter(cls.name == tag_name).first()
        if existing_tag:
            return existing_tag
        new_tag = cls(name=tag_name)
        session.add(new_tag)
        return new_tag