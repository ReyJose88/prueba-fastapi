from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserRead, UserCreate
from app.models import User as User_model
from app.core.database import get_db
from app.repositories.user import UserRepository
from app.core.security import hash_password

router = APIRouter()

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    existing = await repo.get_by_email(user.email)
    if existing:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "El email se encuentra registrado")
    user = User_model(
        email=user.email,
        name=user.name,
        password=hash_password(user.password)
    )
    return await repo.create(user)