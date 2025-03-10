from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from models.ReferralCodeCreate import ReferralCodeCreate
from repositories.ReferralCode import ReferralCodeRepository


class ReferralCodeService:
    def __init__(self, referral_code_repository=ReferralCodeRepository):
        self.referral_code_repository = referral_code_repository

    async def create_code(
        self,
        session: AsyncSession,
        referral_code: ReferralCodeCreate,
        creator_id: int,
    ):
        code = await self.referral_code_repository.get_code(session, referral_code.code)
        if code is not None:
            raise HTTPException(status_code=409, detail="Code already exists")
        check = await self.referral_code_repository.check_code(session, creator_id)
        if check is not None:
            raise HTTPException(
                status_code=409, detail="You already have a referral code."
            )
        res = await self.referral_code_repository.create_code(
            session, referral_code, creator_id
        )
        return res

    async def delete_code(
        self,
        session: AsyncSession,
        creator_id: int,
    ):
        code = await self.referral_code_repository.check_code(session, creator_id)
        if code is None:
            raise HTTPException(
                status_code=409, detail="You don't have a referral code"
            )
        res = await self.referral_code_repository.delete_code(session, creator_id)
        return res

    async def get_code(
        self, session: AsyncSession, creator_id: int
    ) -> ReferralCodeCreate:
        res = await self.referral_code_repository.check_code(session, creator_id)
        if res is None:
            raise HTTPException(
                status_code=409, detail="You don't have a referral code"
            )
        ref_code = ReferralCodeCreate(code=res.code, date_expired=res.date_expired)
        return ref_code
