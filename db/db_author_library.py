from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm.session import Session
from .author_feed import authors
import time
from .models import Orm_Author

def db_feed(db: Session):
    new_author_list = [Orm_Author(
            author=author["author"],
        ) for author in authors] 
    db.query(Orm_Author).delete()
    db.commit()
    db.add_all(new_author_list)
    db.commit()
    return db.query(Orm_Author).all()
