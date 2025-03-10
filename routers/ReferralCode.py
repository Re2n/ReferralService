from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_mail import FastMail
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from config.Database import db
from config.Mail import conf
from models.Email import Email
from models.ReferralCodeCreate import ReferralCodeCreate
from utils.depends import auth_service, referral_code_service
from utils.mail import create_message

referral_code_router = APIRouter(tags=["Referral Code"])

@referral_code_router.post('/create_referral_code/')
async def create_referral_code(
        session: Annotated[AsyncSession, Depends(db.session_getter)],
        referral_code: ReferralCodeCreate,
        payload: dict = Depends(auth_service.get_current_token_payload),
):
    res = await referral_code_service.create_code(
        session,
        referral_code,
        payload.get("id"),
    )
    return res

@referral_code_router.delete('/delete_referral_code/')
async def delete_referral_code(
        session: Annotated[AsyncSession, Depends(db.session_getter)],
        payload: dict = Depends(auth_service.get_current_token_payload),
):
    res = await referral_code_service.delete_code(session, payload.get("id"))
    return res

@referral_code_router.get('/get_referral_code_by_email/{email}')
async def get_referral_code_by_email(
        session: Annotated[AsyncSession, Depends(db.session_getter)],
        email: EmailStr,
        payload: dict = Depends(auth_service.get_current_token_payload),
):
    code = await referral_code_service.get_code(
        session,
        payload.get("id")
    )
    fm = FastMail(conf)
    msg = await create_message(email, code)
    await fm.send_message(msg)
    return {"detail": "Email has been sent"}