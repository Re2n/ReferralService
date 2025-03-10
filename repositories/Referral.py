from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.Referral import Referral


class ReferralRepository:
    async def create_referral(
        self,
        session: AsyncSession,
        referrer_id: int,
        referral_id: int,
    ):
        stmt = insert(Referral).values(referrer=referrer_id, user_id=referral_id)
        await session.execute(stmt)
        await session.commit()
