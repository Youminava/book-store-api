from sqlalchemy.ext.asyncio import AsyncSession
from app.models.book import BookOrm
from app.schemas.book import BookUpdate


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