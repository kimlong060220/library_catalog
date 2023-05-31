from fastapi import APIRouter
from typing import List

from rating.schema import Rating
from data.database import Database
from book.service import BookService
from rating.service import RatingService
from rating.schema import Rating


router = APIRouter()
ratingService = RatingService()

@router.post("/book/{book_id}/reviews")
def add_views(rating: Rating):
    ratingService.add_rating(rating)