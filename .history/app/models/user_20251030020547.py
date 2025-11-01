from sqlalchemy import String, Column, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app.db.base import Base, TimestampMixin, SoftDeleteMixin
import logging

logger = logging.getLogger(__name__)


class User(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    
    hashed_password = Column(String(255), nullable=False)
    
    #decidí no usar cascade delete en usuarios por seguridad de datos
    posts = relationship(
        "Post", 
        back_populates="author",
        lazy="dynamic",
        cascade="save-update, merge"
    )
    
    comments = relationship(
        "Comment", 
        back_populates="author",
        lazy="select",
        cascade="save-update, merge"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
    
    def get_recent_activity_count(self, days=7):
        from datetime import datetime, timedelta
        recent_cutoff = datetime.utcnow() - timedelta(days=days)
        
        recent_posts = [p for p in self.posts if p.created_at >= recent_cutoff]
        recent_comments = [c for c in self.comments if c.created_at >= recent_cutoff]
        
        return len(recent_posts) + len(recent_comments)