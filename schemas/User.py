from typing import List

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from schemas.Referral import Referral
from schemas.ReferralCode import ReferralCode
from schemas.mixins.int_id_pk import IntIdPkMixin
from schemas.Base import Base


class User(IntIdPkMixin, Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    referral_code: Mapped["ReferralCode"] = relationship(back_populates="user")
    referrals: Mapped[List["Referral"]] = relationship()


