from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, Optional
from app.database import Base
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Text, String, DateTime, ForeignKey
from enum import Enum

class Genres(Enum):
    FANTASY = "fantasy" 
    DETECTIVE = "detective" 
    ADVENTURE = "adventure" 
    HORROR = "horror" 
    NOVEL = "novel" 

if TYPE_CHECKING:
    from app.models.author import AuthorOrm

class BookOrm(Base):
    __tablename__ = "books"
    
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    genre: Mapped[Genres] = mapped_column(nullable=False)
    author_id: Mapped[str] = mapped_column(String(36), ForeignKey("authors.id"), nullable=False)
    author: Mapped[AuthorOrm] = relationship("AuthorOrm", back_populates="books")
    year_of_publication: Mapped[Optional[int]] = mapped_column(default=None)
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)
    price: Mapped[float]
    quantity: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    isbn: Mapped[str] = mapped_column(unique=True)