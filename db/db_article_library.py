from typing import List
from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm.session import Session
from .article_feed import articles
import time
from .models import Orm_Article

def db_feed(db: Session):
    new_article_list = [Orm_Article(
            title=article["title"],
            author=article["author"],
            description=article["description"],
            content=article["content"]
        ) for article in articles] 
    db.query(Orm_Article).delete()
    db.commit()
    db.add_all(new_article_list)
    db.commit()
    return db.query(Orm_Article).all()


def get_all(db: Session) -> List[Orm_Article]:
    return db.query(Orm_Article).all()

def get_article_by_id(id: int, db: Session):
    return db.query(Orm_Article).filter(Orm_Article.id == id).first()
