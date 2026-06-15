from sqlalchemy.ext.asyncio import AsyncSession
from app.models.author import AuthorOrm
from app.schemas.author import AuthorUpdate, AuthorBase

async def find_author(session: AsyncSession,
                      author_id: str
) -> AuthorOrm | None:
    author = await session.get(AuthorOrm, author_id)
    if author is None:
        return None
    return author

async def update_author(session: AsyncSession, 
                      author_id: str, 
                      payload: AuthorUpdate
) -> AuthorOrm | None:
    author = await session.get(AuthorOrm, author_id)
    if author is None:
        return None

    data = payload.model_dump(exclude_unset=True)   
    for field, value in data.items():
        setattr(author, field, value)

    await session.commit()
    await session.refresh(author)                     
    return author

async def create_author(session: AsyncSession,
                        payload: AuthorBase
) -> AuthorOrm | None:
    author = AuthorOrm(**payload.model_dump())
    if author is None:
        return None
    session.add(author)
    await session.commit()
    await session.refresh(author)
    return author