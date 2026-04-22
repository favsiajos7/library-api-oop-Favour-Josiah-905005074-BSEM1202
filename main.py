from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio

app = FastAPI()

# 📚 Book model (OOP structure)
class Book(BaseModel):
    id: int
    title: str
    author: str
    category: str
    available: bool

# 📖 Borrow request model
class BorrowRequest(BaseModel):
    user_id: int
    book_id: int

# 🔁 Return request model
class ReturnRequest(BaseModel):
    user_id: int
    book_id: int

# 📚 Fake database
books: List[Book] = [
    Book(id=1, title="Python Basics", author="John Smith", category="Programming", available=True),
    Book(id=2, title="Database Systems", author="Mary Brown", category="IT", available=True)
]

# 🏠 Home endpoint
@app.get("/")
async def home():
    return {"message": "Library API is running"}

# 📚 Get all books
@app.get("/books", response_model=List[Book])
async def get_books():
    return books

# 🔎 Search books
@app.get("/books/search", response_model=List[Book])
async def search_books(query: str):
    results = []

    for book in books:
        if (
            query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
            or query.lower() in book.category.lower()
        ):
            results.append(book)

    return results

# 📖 Borrow book (ASYNC + ERROR HANDLING)
@app.post("/borrow")
async def borrow_book(request: BorrowRequest):

    await asyncio.sleep(1)  # simulate real system delay

    for book in books:
        if book.id == request.book_id:

            if not book.available:
                raise HTTPException(status_code=400, detail="Book already borrowed")

            book.available = False

            return {
                "message": f"User {request.user_id} borrowed '{book.title}' successfully",
                "book_id": book.id,
                "status": "borrowed"
            }

    raise HTTPException(status_code=404, detail="Book not found")

# 🔁 Return book (ASYNC + STATE UPDATE)
@app.post("/return")
async def return_book(request: ReturnRequest):

    await asyncio.sleep(1)  # simulate real system delay

    for book in books:
        if book.id == request.book_id:

            if book.available:
                return {
                    "message": "Book was not borrowed",
                    "status": "info"
                }

            book.available = True

            return {
                "message": f"User {request.user_id} returned '{book.title}' successfully",
                "book_id": book.id,
                "status": "returned"
            }

    raise HTTPException(status_code=404, detail="Book not found")