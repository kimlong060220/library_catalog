from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    publication_year: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class MemberBase(BaseModel):
    name: str
    membership_id: int


class MemberCreate(MemberBase):
    pass


class MemberUpdate(MemberBase):
    pass
