from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from jardinier.database.base import Base


class Measure(Base):
    """User ORM example"""
    __tablename__ = "measure"

    time: Mapped[datetime] = mapped_column(primary_key=True, index=True)
    temperature: Mapped[float] = mapped_column()
    humidity: Mapped[float] = mapped_column()
