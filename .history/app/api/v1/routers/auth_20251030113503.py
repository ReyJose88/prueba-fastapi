from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import LoginRequest, Token
from app.core.database import get_db
from app.repositories.user import UserRepository
from app.services.auth import authenticate_user, create_token_for_user

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    user_repo = UserRepository(db)
    user = await authenticate_user(form_data.email, form_data.password, user_repo)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return create_token_for_user(user.id)