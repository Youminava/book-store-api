from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from uuid import uuid4
from typing import Optional

class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda:str(uuid4()))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    phone_number: Mapped[Optional[str]] = mapped_column(default=None)
    name: Mapped[str] = mapped_column(String(55))
    reviews: Mapped[list["ReviewOrm"]] = relationship("ReviewOrm", back_populates="user")
    hashed_password: Mapped[str]