from app.repositories.user import UserRepository
from app.core.security import verify_password, create_access_token, create_refresh_token
from app.schemas.auth import Token
from datetime import timedelta
from app.core.config import settings

async def verify_password_user(email: str, password: str, user_repo: UserRepository):
    user = await user_repo.get_by_email(email)
    if not user or not verify_password(password, user.password):
        return None
    return user

def create_token_user(user: UserRepository) -> Token:
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    new_access_token = create_access_token(data={"sub": user.email, "user_id": user.id}, expires_delta=access_token_expires)
    new_refresh_token = create_refresh_token(data={"sub": user.email, "user_id": user.id}, expires_delta=refresh_token_expires)

    return Token(access_token=new_access_token, refresh_token=new_refresh_token, token_type="bearer")
    '''access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user_id)}, expires_delta=access_token_expires
    )
    return generate_new_tokens(user)
'''

def generate_new_tokens(user):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    new_access_token = create_access_token(data={"sub": user.email, "user_id": user.id}, expires_delta=access_token_expires)
    new_refresh_token = create_refresh_token(data={"sub": user.email, "user_id": user.id}, expires_delta=refresh_token_expires)

    return Token(access_token=new_access_token, refresh_token=new_refresh_token, token_type="bearer")
    '''
    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }'''