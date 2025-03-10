from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from models.UserCreate import UserCreate
from schemas.Referral import Referral
from schemas.User import User
from utils import auth


class UserRepository:
    async def create_user(
            self,
            session: AsyncSession,
            user: UserCreate
    ) -> UserCreate:
        hash_password = auth.hash_password(user.password)
        stmt = insert(User).values(email=user.email, password=hash_password)
        await session.execute(stmt)
        await session.commit()
        return user

    async def get_user(
            self, session:
            AsyncSession,
            email: str
    ) -> User:
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        return result.scalar()

    async def get_referrals(
            self,
            session: AsyncSession,
            referrer_id: int,
    ):
        stmt = select(User).join(Referral, Referral.user_id == User.id).where(Referral.referrer == referrer_id)
        result = await session.execute(stmt)
        return result.scalars().all()