from fastapi import APIRouter

from book.service import BookService
from book.schema import Book, BookCreateSchema, BookUpdateSchema

router = APIRouter()
book_service = BookService()


@router.get("/books")
def get_books():
    books = book_service.get_books()
    return books


@router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = book_service.get_book(book_id)
    return book


@router.post("/books", response_model=Book)
def create_book(book_data: BookCreateSchema):
    book = book_service.create_book(book_data)
    return book


@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookUpdateSchema):
    book = book_service.update_book(book_id, book_data)
    return book


@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    book_service.delete_book(book_id)
    return {"message": "Book deleted successfully"}
