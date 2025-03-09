from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.UserCreate import UserCreate
from repositories.User import UserRepository
from schemas.User import User


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, session: AsyncSession, user: UserCreate):
        stmt = select(User).where(User.email == user.email)
        result = await session.execute(stmt)
        if result.scalar():
            raise HTTPException(status_code=409, detail="User already exists")
        new_user = await self.repository.create_user(session, user)
        return new_user