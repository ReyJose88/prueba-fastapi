from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.post import PostRead, PostCreate
from app.models import User, Post, Tag
from app.api.v1.deps import get_current_user
from app.core.database import get_db
from app.repositories.post import PostRepository
from app.repositories.tag import TagRepository

router = APIRouter()

@router.post("/", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_in: PostCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    post_repo = PostRepository(db)
    tag_repo = TagRepository(db)

    tags = []
    for tag_name in post_in.tags or []:
        tag = await tag_repo.get_by_name(tag_name)
        if not tag:
            tag = Tag(name=tag_name)
            tag = await tag_repo.create(tag)
        tags.append(tag)

    post = Post(
        title=post_in.title,
        content=post_in.content,
        user_id=current_user.id,
        tags=tags
    )
    created_post = await post_repo.create(post)
    
    return await post_repo.get_active_with_relations(created_post.id)

@router.get("/", response_model=list[PostRead])
async def list_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    repo = PostRepository(db)
    return await repo.list_active_with_relations(skip=skip, limit=limit)

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    repo = PostRepository(db)
    post = await repo.get_active(post_id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post no contrado")

    success = await repo.soft_delete(post_id)
    if not success:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "La eliminacion fallo")
