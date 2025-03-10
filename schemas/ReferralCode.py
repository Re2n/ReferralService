from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from schemas.Base import Base
from schemas.mixins.int_id_pk import IntIdPkMixin


class ReferralCode(IntIdPkMixin, Base):
    __tablename__ = "referral_code"

    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    date_expired: Mapped[datetime] = mapped_column()
    creator: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
