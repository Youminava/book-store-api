from fastapi import Depends, HTTPException, APIRouter
from app.repositories.author import find_author, update_author, create_author
from app.schemas.author import AuthorUpdate, Author, AuthorBase
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
router = APIRouter(prefix="/author", tags=["Авторы"])

@router.patch("/{author_id}", response_model=Author)
async def patch_author(author_id: str, 
                 payload: AuthorUpdate, 
                 session: AsyncSession = Depends(get_db)
):
    author = await update_author(session=session, author_id=author_id, payload=payload)
    if author is None:
        raise HTTPException(status_code=404, detail="Автор не найден")
    return author

@router.get("/{author_id}", response_model=Author)
async def get_author(author_id: str,
                      session: AsyncSession = Depends(get_db)
):
    author = await find_author(session=session, author_id=author_id)
    if author is None:
        return HTTPException(status_code=404, detail="Автор не найден")
    return author

@router.post("", response_model=Author)
async def post_author(payload: AuthorBase,
                      session: AsyncSession = Depends(get_db)
):
    author = await create_author(session=session, payload=payload)
    if author is None:
        return HTTPException(status_code=404, detail="Автор не найден")
    return author