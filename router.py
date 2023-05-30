from fastapi import FastAPI
from typing import List
from fastapi import HTTPException
from schema import BookCreate, BookUpdate, MemberCreate, MemberUpdate
from service import LibraryService

app = FastAPI()
library_service = LibraryService()


@app.post("/books", response_model=BookCreate)
def create_book(book: BookCreate):
    return library_service.create_book(book)


@app.get("/books/{book_id}", response_model=BookCreate)
def get_book(book_id: int):
    book = library_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=BookCreate)
def update_book(book_id: int, book: BookUpdate):
    updated_book = library_service.update_book(book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@app.get("/books", response_model=List[BookCreate])
def get_all_books():
    return library_service.get_all_books()


@app.post("/members", response_model=MemberCreate)
def create_member(member: MemberCreate):
    return library_service.create_member(member)


@app.get("/members/{member_id}", response_model=MemberCreate)
def get_member(member_id: int):
    member = library_service.get_member(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@app.put("/members/{member_id}", response_model=MemberCreate)
def update_member(member_id: int, member: MemberUpdate):
    updated_member = library_service.update_member(member_id, member)
    if not updated_member:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated_member


@app.get("/members", response_model=List[MemberCreate])
def get_all_members():
    return library_service.get_all_members()
