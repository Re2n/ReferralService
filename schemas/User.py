from typing import List

from pydantic_core.core_schema import nullable_schema
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from schemas import Referral
from schemas import ReferralCode
from schemas.mixins.int_id_pk import IntIdPkMixin
from schemas.Base import Base


class User(IntIdPkMixin, Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=False)


