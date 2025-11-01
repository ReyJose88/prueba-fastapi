from app.repositories.user import UserRepository
from app.core.security import verify_password, create_access_token
from app.schemas.auth import Token
from datetime import timedelta
from app.core.config import settings

async def authenticate_user(email: str, password: str, user_repo: UserRepository):
    user = await user_repo.get_by_email(email)
    if not user or not verify_password(password, user.password):
        return None
    return user

def create_token_for_user(user_id: int) -> Token:
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user_id)}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")