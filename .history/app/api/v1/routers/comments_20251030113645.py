from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from app.api.v1.deps import get_current_user
from app.core.database import get_db
from app.repositories.comment import CommentRepository
from app.repositories.post import PostRepository

router = APIRouter()

@router.post("/posts/{post_id}/comments", response_model=schemas.CommentRead, status_code=status.HTTP_201_CREATED)
async def create_comment(
    post_id: int,
    comment_in: schemas.CommentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    post_repo = PostRepository(db)
    post = await post_repo.get_active(post_id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")

    comment = models.Comment(
        content=comment_in.content,
        author_id=current_user.id,
        post_id=post_id
    )
    repo = CommentRepository(db)
    return await repo.create(comment)