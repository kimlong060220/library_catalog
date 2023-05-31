from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from book import router as book_router
from member import router as member_router
from rating import router as rating_router
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router.router)
app.include_router(member_router.router)
app.include_router(rating_router.router)