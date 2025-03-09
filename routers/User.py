from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.Database import db
from models.UserCreate import UserCreate
from utils.depends import user_service

user_router = APIRouter(tags=['User'])

@user_router.post('/register',
                  response_model=UserCreate,
                  response_model_exclude_none=True
)
async def register_user(
        session: Annotated[AsyncSession, Depends(db.session_getter)],
        user: UserCreate | None = None,
):
    res = await user_service.create_user(session, user)
    return res