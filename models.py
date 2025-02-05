from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Author:
    id: int
    name: str
    books: List['Book']

@dataclass
class Book:
    id: int
    title: str
    author_id: int
    published_year: int
    description: Optional[str] = None

# Sample data
books_db = [
    Book(id=1, title="The Great Gatsby", author_id=1, published_year=1925),
    Book(id=2, title="To Kill a Mockingbird", author_id=2, published_year=1960),
    Book(id=3, title="1984", author_id=3, published_year=1949),
]

authors_db = [
    Author(id=1, name="F. Scott Fitzgerald", books=[]),
    Author(id=2, name="Harper Lee", books=[]),
    Author(id=3, name="George Orwell", books=[]),
]

# Update author's books
for author in authors_db:
    author.books = [book for book in books_db if book.author_id == author.id]
