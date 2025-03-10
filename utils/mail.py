from fastapi_mail import MessageSchema

from models.ReferralCodeCreate import ReferralCodeCreate


async def create_template(referral_code: ReferralCodeCreate):
    template = f"""
            <html>
            <body>
                <p><br>Your referral code: {referral_code.code}<br></p>
                <p><br>Date expired: {referral_code.date_expired}<br></p>
            </body>
            </html>
    """
    return template


async def create_message(email: str, referral_code: ReferralCodeCreate):
    msg = MessageSchema(
        subject="Referral Service",
        recipients=[email],
        body=await create_template(referral_code),
        subtype="html",
    )
    return msg
