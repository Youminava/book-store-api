from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
from app.models.book import Genres

class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    author_id: str
    year_of_publication: Optional[int] = Field(default=None)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
    isbn: str
    genre: Genres
    @field_validator("title")
    @classmethod
    def validate_title(cls, v: Optional[str]) -> Optional[str]:
        if v is None:                     
            return v
        v = v.strip()
        if not v:
            raise ValueError("Название не может быть пустым")
        if not v.isprintable():
            raise ValueError("Название содержит непечатаемые символы")
        return v

    @field_validator("year_of_publication")
    @classmethod
    def validate_year_of_publication(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        if v > datetime.now().year:
            raise ValueError("Год публикации не может быть в будущем")
        return v

class BookUpdate(BookBase):
    title: Optional[str] = None
    author_id: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    quantity: Optional[int] = Field(default=None, gt=0)
    isbn: Optional[str] = None
    updated_at: Optional[datetime] = Field(default=datetime.now())

class Book(BookBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True} 
