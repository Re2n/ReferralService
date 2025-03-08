from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from schemas.Base import Base
from schemas.User import User
from schemas.mixins.int_id_pk import IntIdPkMixin


class ReferralCode(IntIdPkMixin, Base):
    __tablename__ = "referral_code"

    code: Mapped[str] = mapped_column(nullable=False)
    date_expired: Mapped[datetime] = mapped_column()
    user: Mapped["User"] = relationship(back_populates="referral_code")
