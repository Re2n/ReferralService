from sqlalchemy.ext.asyncio import AsyncSession

from models.UserCreate import UserCreate
from schemas.User import User


class UserRepository:
    async def create_user(self, session: AsyncSession, user: UserCreate) -> UserCreate:
        new_user = User(**user.model_dump())
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return user