from pydantic import BaseModel, Field, field_validator
from datetime import date

class AuthorBase(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    surname: str = Field(min_length=1, max_length=30)
    patronymic: str = Field(min_length=1, max_length=30)
    bio: str | None = Field(default=None, max_length=300)
    birth_date: date
    death_date: date | None = Field(default=None)
    books: list

class AuthorUpdate(AuthorBase):
    name: str | None = Field(default=None)
    surname: str | None = Field(default=None)
    patronymic: str | None = Field(default=None)
    birth_date: date | None= Field(default=None)
    books: list | None = Field(default=None)

class Author(AuthorBase):
    id: str

    model_config = {"from_attributes": True} 