from data.database import Database
from book.schema import Book, BookCreateSchema, BookUpdateSchema
from rating.schema import Rating

class BookService:
    def __init__(self):
        self.db = Database()

    def get_books(self):
        query = """
            SELECT * FROM books;
        """
        books = self.db.execute_query(query)
        return books

    def get_book(self, book_id: int):
        query = "SELECT * FROM books WHERE id = %s"
        params = (book_id,)
        book_data = self.db.execute_query(query, params)
        if book_data:
            book = Book(
                title= book_data[0][1],
                author= book_data[0][2],
                publication_year=book_data[0][3],
                category=book_data[0][4],
                description=book_data[0][5],
                rating=book_data[0][6]
            )
            return book
        else:
            return None

    def create_book(self, book_data: BookCreateSchema) -> Book:
        query = """INSERT INTO books (title, author, publication_year, category, description, rating) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
        book_data.get_book_info()
        params = (
            book_data.title, 
            book_data.author, 
            book_data.publication_year, 
            book_data.category, 
            book_data.description, 
            book_data.rating)
        book_id = self.db.execute_query(query, params)
        book = Book(id=book_id, **book_data.dict())
        return book

    def update_book(self, book_id: int, book_data: BookUpdateSchema):
        query = """
        UPDATE books 
        SET title = %s, author = %s, publication_year = %s, category = %s, description = %s, rating = %s
        WHERE id = %s;
        """
        params = (
            book_data.title,
            book_data.author,
            book_data.publication_year,
            book_data.category,
            book_data.description,
            book_data.rating,
            book_id,
        )
        # rows_affected = self.db.execute_query(query, params)
        # if len(rows_affected) > 0:
        #     book = Book(id=book_id, **book_data.dict())
        #     return book
        # return None

    def delete_book(self, book_id: int):
        query = "DELETE FROM books WHERE id = %s"
        params = (book_id,)
        rows_affected = self.db.execute_query(query, params)
        return rows_affected > 0   

    def get_book_ratings(self, book_id: int):
        query = "SELECT rating FROM ratings WHERE book_id = %s"
        params = (book_id,)
        ratings = self.db.execute_query(query, params)
        return ratings
    
    def update_book_rating(self, book_id):
        book = self.get_book(book_id)
        ratings = self.get_book_ratings(book_id)
        print(book)
        if ratings:
            total_rating = sum(rating[0] for rating in ratings)
            aveger_rating = total_rating/ len(ratings)
            book.rating = aveger_rating
            self.update_book(book_id, book)
        else:
            book.rating = 0.0
            self.update_book(book_id,book)


