# Bookstore Application

A full-stack bookstore application built with FastAPI and Vue.js.

## Project Structure
```
bookstore/
├── backend/
│   ├── main.py          # FastAPI application
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   └── database.py      # Database configuration
└── frontend/
    └── src/
        ├── components/  # Vue components
        └── pages/       # Vue pages
```

## Backend Setup

1. Create virtual environment:
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install fastapi sqlalchemy uvicorn
```

3. Run the server:
```bash
uvicorn main:app --reload
```

## Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run development server:
```bash
npm run dev
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /get-books/ | List all books |
| POST   | /add_book | Add new book |
| PUT    | /update-book/{book_id} | Update book |
| DELETE | /delete-book/{book_id} | Delete book |

## Environment Variables
Create `.env` file in backend directory:
```
DATABASE_URL=sqlite:///./bookstore.db
```