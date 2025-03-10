from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jwt.exceptions import InvalidTokenError
from models.UserCreate import UserResponse, UserCreate
from repositories.User import UserRepository
from utils import auth

http_bearer = HTTPBearer()

class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def validate_auth_user(
            self,
            session: AsyncSession,
            user: UserCreate
        ) -> UserResponse:
        res = await self.repository.get_user(session, user.email)
        exc = HTTPException(status_code=401, detail='Invalid credentials')
        if res is None:
            raise exc
        if not auth.validate_password(
            password=user.password,
            hashed_password=res.password,
        ):
            raise exc

        return UserResponse(id=res.id, email=res.email)

    async def get_current_token_payload(
        self,
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer)
        ) -> dict:
        token = credentials.credentials
        try:
            payload = auth.decode_jwt(
                token=token,
            )
        except InvalidTokenError:
            raise HTTPException(
                status_code=401,
                detail=f"Token invalid",
            )
        return payload


    async def get_current_auth_user(
            self,
            session: AsyncSession,
            payload: dict = Depends(get_current_token_payload),
        ) -> UserResponse:
        email: str | None = payload.get("sub")
        res = await self.repository.get_user(session, email)
        if res is not None:
            return UserResponse(id=res.id, email=res.email)

        raise HTTPException(
            status_code=401,
            detail="Token invalid",
        )