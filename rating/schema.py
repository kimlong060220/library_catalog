from pydantic import BaseModel


class Rating(BaseModel):
    member_id: int
    book_id: int
    rating: int
