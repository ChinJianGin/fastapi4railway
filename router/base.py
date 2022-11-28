from .article import article_router

from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(article_router.router, prefix="/api/article", tags=["article"])
