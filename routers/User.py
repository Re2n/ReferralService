from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.Database import db
from models.UserCreate import UserCreate, UserCreateResponse
from utils.TokenInfo import TokenInfo
from utils.depends import user_service, auth_service
from utils import auth

user_router = APIRouter(tags=['User'])

@user_router.post('/register/')
async def register_user(
        session: Annotated[AsyncSession, Depends(db.session_getter)],
        user: UserCreate,
) -> UserCreate:
    res = await user_service.create_user(session, user)
    return res

@user_router.post("/login/")
async def auth_user_issue_jwt(
    session: Annotated[AsyncSession, Depends(db.session_getter)],
    user: UserCreate,
):
    res = await auth_service.validate_auth_user(session, user)
    jwt_payload = {
        "sub": res.email,
        "email": res.email,
    }
    token = auth.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )

@user_router.get("/me/")
async def auth_user_check_self_info(
    session: Annotated[AsyncSession, Depends(db.session_getter)],
    payload: dict = Depends(auth_service.get_current_token_payload),
):
    user = await auth_service.get_current_auth_user(session, payload)
    iat = payload.get("iat")
    return {
        "email": user.email,
        "logged_in_at": iat,
    }