from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas import ArticleResponse, AuthorResponse, CommentResponse, ArticleResponseWithLikesAndComments
from db.database import get_db
from db import db_article_library, db_author_library, db_comment_library

router = APIRouter()

@router.get('/feed', response_model=List[ArticleResponse])
def feed_initial_articles(db: Session = Depends(get_db)):
    return db_article_library.db_feed(db)

@router.get('/author/feed', response_model=List[AuthorResponse])
def feed_initial_authors(db: Session = Depends(get_db)):
    return db_author_library.db_feed(db)

@router.get('/comment/feed', response_model=List[CommentResponse])
def feed_initial_comments(db: Session = Depends(get_db)):
    return db_comment_library.db_feed(db)

@router.get('/all', response_model=List[ArticleResponse])
def get_all_article(db: Session = Depends(get_db)):
    return db_article_library.get_all(db)

@router.get('/id', response_model=ArticleResponseWithLikesAndComments)
def get_article_by_id(id: int, db: Session = Depends(get_db)):
    return db_article_library.get_article_by_id(id, db)
