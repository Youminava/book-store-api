from fastapi import FastAPI
from app.routes import book_router, author_router

app = FastAPI()
app.include_router(book_router)
app.include_router(author_router)