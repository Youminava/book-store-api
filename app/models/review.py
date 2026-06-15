from sqlalchemy import Float, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from uuid import uuid4
from datetime import datetime
from app.database import Base

class ReviewOrm(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 10", name="ck_reviews_rating_range"),
    )

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda:str(uuid4()))
    book_id: Mapped[str] = mapped_column(ForeignKey("books.id"), nullable=False)
    book: Mapped["BookOrm"] = relationship("BookOrm", back_populates="reviews")
    user: Mapped["UserOrm"] = relationship("UserOrm", back_populates="reviews")
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)
    rating: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)