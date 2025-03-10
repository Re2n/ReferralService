from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from schemas.Base import Base
from schemas.mixins.int_id_pk import IntIdPkMixin


class Referral(IntIdPkMixin, Base):
    __tablename__ = "referral"

    referrer: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
