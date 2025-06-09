from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    qty: int = 0

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    qty: Optional[int] = None

class BookResponse(BaseModel):
    book_id: int
    title: str
    author: str
    price: float
    qty: int
    
    class Config:
        from_attributes = True