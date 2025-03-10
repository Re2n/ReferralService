from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from schemas.mixins.int_id_pk import IntIdPkMixin
from schemas.Base import Base


class User(IntIdPkMixin, Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=False)
