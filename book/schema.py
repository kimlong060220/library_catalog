from pydantic import BaseModel
from typing import List, Optional


class Book(BaseModel):
    title: str
    author: str
    publication_year: int
    category: str
    description: Optional[str]
    rating: float
    
    def get_book_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nRating: {self.rating}"

class BookCreateSchema(Book):
    pass

class BookUpdateSchema(Book):
    id: int

class BookResponseSchema(Book):
    id: int

class BookListResponseSchema(BaseModel):
    books: List[BookResponseSchema]
