# Library API System using FastAPI (OOP Project)

## Description
This project is a Library Management API built using FastAPI and Object-Oriented Programming (OOP) principles. It allows users to search for books, borrow books, and return books through a simple and efficient RESTful API system. The system simulates a real-world library where multiple users can interact with the system at the same time.

## Features

- Search for books by title, author, or category  
- Borrow books with user tracking  
- Return borrowed books  
- Track book availability status  
- Prevent double borrowing of the same book  
- RESTful API design using FastAPI  
- OOP-based Book model structure  
- Asynchronous operations for realistic system simulation  



## Technologies Used

- Python  
- FastAPI  
- Pydantic  
- Uvicorn  
- AsyncIO  
- Git & GitHub  

## How to Run the Project

Install dependencies: pip install -r requirements.txt
Run the server: uvicorn main:app --reload
Open API in browser: http://127.0.0.1:8000/docs

## Test Endpoints
- GET /books 
- GET /books/search?query=python
- POST /borrow
- POST /return

