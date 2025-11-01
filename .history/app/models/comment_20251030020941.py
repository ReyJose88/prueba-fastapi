from sqlalchemy import String, Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin, SoftDeleteMixin

class Comment(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, index=True)

    author = relationship(
        "User", 
        back_populates="comments",
        lazy="joined"
    )
    
    post = relationship(
        "Post", 
        back_populates="comments",
        lazy="select"
    )

    def __repr__(self):
        return f"<Comment(id={self.id}, author_id={self.author_id})>"

    @property
    def excerpt(self):
        if len(self.content) > 50:
            return self.content[:47] + "..."
        return self.content

    def is_editable(self, user_id, time_limit_hours=24):
        from datetime import datetime, timedelta
        if self.author_id != user_id:
            return False
        time_limit = datetime.utcnow() - timedelta(hours=time_limit_hours)
        return self.created_at >= time_limit