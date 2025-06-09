from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, Book
from schemas import BookCreate, BookResponse, BookUpdate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:8000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bookstore API!"}

@app.post("/add_book", response_model=BookResponse)
def add_book(book_data: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        price=book_data.price,
        qty=book_data.qty
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/get-books/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

@app.put("/update-book/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    # Find the book by ID
    book = db.query(Book).filter(Book.book_id == book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Update only the fields that are provided
    update_data = book_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)
    
    db.commit()
    db.refresh(book)
    return book

@app.delete("/delete-book/{book_id}", response_model=BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    # Find the book by ID
    book = db.query(Book).filter(Book.book_id == book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Delete the book
    db.delete(book)
    db.commit()
    return book