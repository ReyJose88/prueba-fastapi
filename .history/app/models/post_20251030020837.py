from sqlalchemy import String, Column, Integer, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin, SoftDeleteMixin

post_tag = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)


class Post(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True) 
    
    content = Column(Text, nullable=False)
    
    author_id = Column(Integer, ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)

    author = relationship(
        "User", 
        back_populates="posts",
        lazy="joined"
    )
    
    comments = relationship(
        "Comment", 
        back_populates="post",
        cascade="all, delete-orphan",  
        lazy="dynamic",  
        order_by="Comment.created_at.desc()" 
    )
    
    tags = relationship(
        "Tag", 
        secondary=post_tag, 
        back_populates="posts",
        lazy="select", 
        cascade="save-update" 
    )
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title[:30]}...')>"
    
    def has_inappropriate_content(self, banned_words_list=None):
        if not banned_words_list:
            banned_words_list = ['spam', 'scam', 'phishing']
            
        content_lower = self.content.lower()
        return any(word in content_lower for word in banned_words_list)
    
    @property
    def tag_names(self):
        return [tag.name for tag in self.tags] if self.tags else []
    
    def can_user_edit(self, user_id):
        return self.author_id == user_id
