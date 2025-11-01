from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserRead, UserCreate
from app.models import User as User_model
from app.core.database import get_db
from app.repositories.user import UserRepository
from app.core.security import hash_password

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    existing = await repo.get_by_email(user_in.email)
    if existing:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Email already registered")
    user = User_model(
        email=user_in.email,
        name=user_in.name,
        password=hash_password(user_in.password)
    )
    return await repo.create(user)