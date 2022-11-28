from .database import Base
from sqlalchemy import Text, Column, Integer, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("article.id")),
    Column("right_id", ForeignKey("author.id")),
        )

class Orm_Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    author = Column(Text, nullable=True)
    description = Column(Text, nullable=False)
    content = Column(Text, nullable=True)
    article_comment = relationship("Orm_Comment", back_populates='owner')
    article_like = relationship("Orm_Author", secondary=association_table, back_populates='owner')

class Orm_Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey('article.id'))
    owner_id = Column(Integer, ForeignKey('author.id'))
    comment = Column(Text, nullable=True)
    owner = relationship("Orm_Article", back_populates='article_comment')
    myauthor = relationship("Orm_Author", back_populates='mycomment')


class Orm_Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(Text, nullable=False)
    owner = relationship("Orm_Article", secondary=association_table, back_populates='article_like')
    mycomment = relationship("Orm_Comment", back_populates='myauthor')
