from sqlalchemy.ext.asyncio import AsyncSession
from app.models.book import BookOrm
from app.schemas.book import BookUpdate, BookBase


async def update_book(session: AsyncSession, 
                      book_id: str, 
                      payload: BookUpdate
) -> BookOrm | None:
    book = await session.get(BookOrm, book_id)
    if book is None:
        return None

    data = payload.model_dump(exclude_unset=True)   
    for field, value in data.items():
        setattr(book, field, value)

    await session.commit()
    await session.refresh(book)                     
    return book

async def find_book(session: AsyncSession, 
                    book_id: str
) -> BookOrm | None:
    book = await session.get(BookOrm, book_id)
    if book is None:
        return None
    return book

async def create_book(session: AsyncSession,
                      payload: BookBase
) -> BookOrm | None:
    book = BookOrm(**payload.model_dump())
    if book is None:
        return None
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book