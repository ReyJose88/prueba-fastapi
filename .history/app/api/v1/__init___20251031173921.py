from fastapi import APIRouter
from .routers import auth, register, posts, comments

api_router = APIRouter()
api_router.include_router(register.router, prefix="/auth", tags=["register"])
api_router.include_router(auth.router, prefix="/auth", tags=["login"])
api_router.include_router(auth.router, prefix="/auth", tags=["refresh"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])