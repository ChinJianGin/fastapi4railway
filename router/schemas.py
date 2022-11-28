from typing import List
from pydantic import BaseModel

class ArticleRequest(BaseModel):
    title: str
    author: str
    description: str
    content: str

class ArticleResponse(ArticleRequest):
    id: int

    class Config:
        orm_mode = True

class AuthorRequest(BaseModel):
    author: str

class AuthorResponse(AuthorRequest):
    id: int

    class Config:
        orm_mode = True

class CommentRequest(BaseModel):
    article_id: int
    owner_id: int
    comment: str
    myauthor: AuthorResponse

class CommentResponse(CommentRequest):
    id: int

    class Config:
        orm_mode = True


class ArticleResponseWithLikesAndComments(ArticleRequest):
    id: int
    article_like: List[AuthorResponse]
    article_comment: List[CommentResponse]

    class Config:
        orm_mode = True
