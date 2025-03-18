from sqlalchemy.orm import Mapped, mapped_column

from templates.database.base import Base


class A(Base):
    """User ORM example"""
    __tablename__ = "a"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
