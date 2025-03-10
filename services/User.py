from datetime import datetime

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from models.UserCreate import UserCreate, UserResponse
from repositories.Referral import ReferralRepository
from repositories.ReferralCode import ReferralCodeRepository
from repositories.User import UserRepository


class UserService:
    def __init__(
        self,
        user_repository: UserRepository,
        referral_code_repository: ReferralCodeRepository,
        referral_repository: ReferralRepository,
    ):
        self.user_repository = user_repository
        self.referral_code_repository = referral_code_repository
        self.referral_repository = referral_repository

    async def create_user(
        self,
        session: AsyncSession,
        user: UserCreate,
        referral_code: str,
    ):
        res = await self.user_repository.get_user(session, user.email)
        if res is not None:
            raise HTTPException(status_code=409, detail="User already exists")
        if referral_code:
            ref_code = await self.referral_code_repository.get_code(
                session, referral_code
            )
            if ref_code is None:
                raise HTTPException(status_code=404, detail="Referral code not found")
            if ref_code.date_expired < datetime.now():
                raise HTTPException(status_code=409, detail="Referral code expired")
            new_user = await self.user_repository.create_user(session, user)
            res = await self.user_repository.get_user(session, user.email)
            await self.referral_repository.create_referral(
                session, ref_code.creator, res.id
            )
            return new_user
        new_user = await self.user_repository.create_user(session, user)
        return new_user

    async def get_referrals(
        self, session: AsyncSession, referrer_id: int
    ) -> UserResponse:
        res = await self.user_repository.get_referrals(session, referrer_id)
        refs = ()
        for ref in res:
            refs += (UserResponse(id=ref.id, email=ref.email),)
        return refs
