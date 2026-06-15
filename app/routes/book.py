from app.schemas.book import BookUpdate, Book, BookBase
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.book import update_book, find_book, create_book
from app.database import get_db

router = APIRouter(prefix="/book", tags=["Книги"])

@router.patch("/{book_id}", response_model=Book)
async def patch_book(book_id: str, 
                    payload: BookUpdate, 
                    session: AsyncSession = Depends(get_db)
):
    book = await update_book(session=session, book_id=book_id, payload=payload)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: str,
                    session: AsyncSession = Depends(get_db),
):
    book = await find_book(session=session, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.post("", response_model=Book)
async def post_book(payload: BookBase,
                    session: AsyncSession = Depends(get_db)
):
    book = await create_book(session=session, payload=payload)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book
    