from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from uuid import uuid4
from datetime import datetime
from sqlalchemy import String, Text, DateTime

if TYPE_CHECKING:
    from app.models.book import BookOrm

class AuthorOrm(Base):
    __tablename__ = "authors"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(55), nullable=False)
    surname: Mapped[str] = mapped_column(String(55), nullable=False)
    patronymic: Mapped[Optional[str]] = mapped_column(String(55), default = None)
    bio: Mapped[Optional[str]] = mapped_column(Text, default = None)
    birth_date: Mapped[datetime] = mapped_column(DateTime)
    death_date: Mapped[Optional[datetime]] = mapped_column(DateTime, default=None)
    books: Mapped[list[BookOrm]] = relationship("BookOrm", back_populates="author")