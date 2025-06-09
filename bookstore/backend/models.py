from sqlalchemy import Column, Integer, String, Double
from database import Base

class Book(Base):
    __tablename__ = 'books'
    
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Double, nullable=False)
    qty = Column(Integer, default=0)

