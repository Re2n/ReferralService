from datetime import datetime

from pydantic import BaseModel


class ReferralCodeCreate(BaseModel):
    code: str
    date_expired: datetime = datetime.now()
