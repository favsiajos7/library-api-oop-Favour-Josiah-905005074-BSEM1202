# Library API System using FastAPI (OOP Project)

## Descriptions
This project is a Library Management API built using FastAPI and Object-Oriented Programming (OOP) principles. It allows users to search for books, borrow books, and return books through a simple and efficient RESTful API system. The system is designed to simulate a real-world library where multiple users can interact with the database at the same time.

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

1. Install dependencies:
pip install fastapi uvicorn
uvicorn main:app --reload
http://127.0.0.1:8000/docs

## API Endpoints

- GET / → Home endpoint (checks if API is running)  
- GET /books → Returns all books in the library  
- GET /books/search?query= → Searches books by title, author, or category  
- POST /borrow → Allows a user to borrow a book  
- POST /return → Allows a user to return a borrowed book  

## Project Structure

library-api/
│── main.py
│── README.md
│── requirements.txt
│── .gitignore

## Author

- Name: Favour Sia Josiah  
- Class/semester: BSEM1202/Sem4 
- ID: 905005074

 