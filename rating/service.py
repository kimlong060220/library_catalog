from data.database import Database
from rating.schema import Rating
from book.service import BookService


BookService = BookService()

class RatingService:
    def __init__(self) -> None:
        self.db = Database()

    def add_rating(self, rating: Rating):
        query = "INSERT INTO ratings (book_id, member_id, rating) VALUES (%s, %s, %s)"
        params = (rating.book_id, rating.member_id, rating.rating)
        self.db.execute_query(query, params)
        BookService.update_book_rating(rating.book_id)