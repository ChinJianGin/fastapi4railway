from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm.session import Session
from .comment_feed import comments
import time
from .models import Orm_Comment

def db_feed(db: Session):
    new_comment_list = [Orm_Comment(
            article_id = comment["article_id"],
            owner_id = comment["owner_id"],
            comment= comment["comment"],
        ) for comment in comments] 
    db.query(Orm_Comment).delete()
    db.commit()
    db.add_all(new_comment_list)
    db.commit()
    return db.query(Orm_Comment).all()
