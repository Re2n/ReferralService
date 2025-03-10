from sqlalchemy import select, delete
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from models.ReferralCodeCreate import ReferralCodeCreate
from schemas.ReferralCode import ReferralCode


class ReferralCodeRepository:
    async def get_code(self, session: AsyncSession, referral_code) -> ReferralCode:
        stmt = select(ReferralCode).where(ReferralCode.code == referral_code)
        res = await session.execute(stmt)
        return res.scalar()

    async def create_code(
        self,
        session: AsyncSession,
        referral_code: ReferralCodeCreate,
        creator_id: int,
    ):
        stmt = insert(ReferralCode).values(
            code=referral_code.code,
            date_expired=referral_code.date_expired,
            creator=creator_id,
        )
        await session.execute(stmt)
        await session.commit()
        return referral_code

    async def delete_code(
        self,
        session: AsyncSession,
        creator_id: int,
    ):
        stmt = delete(ReferralCode).where(ReferralCode.creator == creator_id)
        await session.execute(stmt)
        await session.commit()
        return True

    async def check_code(
        self,
        session: AsyncSession,
        creator_id: int,
    ):
        stmt = select(ReferralCode).where(ReferralCode.creator == creator_id)
        res = await session.execute(stmt)
        return res.scalar()
