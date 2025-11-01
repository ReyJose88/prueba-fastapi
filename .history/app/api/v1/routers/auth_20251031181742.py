from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import LoginRequest, Token, RefreshTokenRequest
from app.core.database import get_db
from app.repositories.user import UserRepository
from app.services.auth import verify_password_user, create_token_user, verify_exist_user
from app.core.security import verify_token

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(
    form_data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    user_repo = UserRepository(db)
    user = await verify_password_user(form_data.email, form_data.password, user_repo)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return create_token_user(user)

@router.post("/refresh", response_model=Token)
async def refresh_token(
    refresh_request: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db)
):
    
    token_decode = verify_token(refresh_request.refresh_token)
    
    if not token_decode or token_decode.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token inválido",
        )
    
    email = token_decode.get("sub")
    
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
        )
    #se verifica que el usuario aun exista
    repo = UserRepository(db)
    verify_exist_user(email, repo)

    return create_token_user(user)