import strawberry
from typing import List, Optional
from models import Author, Book, authors_db, books_db

@strawberry.type
class BookType:
    id: int
    title: str
    author_id: int
    published_year: int
    description: Optional[str] = None

    @strawberry.field
    def author(self) -> 'AuthorType':
        return next(author for author in authors_db if author.id == self.author_id)

@strawberry.type
class AuthorType:
    id: int
    name: str
    books: List[BookType]

@strawberry.type
class Query:
    @strawberry.field
    def book(self, id: int) -> Optional[BookType]:
        return next((book for book in books_db if book.id == id), None)

    @strawberry.field
    def books(self) -> List[BookType]:
        return books_db

    @strawberry.field
    def author(self, id: int) -> Optional[AuthorType]:
        return next((author for author in authors_db if author.id == id), None)

    @strawberry.field
    def authors(self) -> List[AuthorType]:
        return authors_db

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(
        self, 
        title: str, 
        author_id: int, 
        published_year: int, 
        description: Optional[str] = None
    ) -> BookType:
        # Check if author exists
        author = next((a for a in authors_db if a.id == author_id), None)
        if not author:
            raise ValueError(f"Author with id {author_id} not found")

        # Create new book
        new_book = Book(
            id=len(books_db) + 1,
            title=title,
            author_id=author_id,
            published_year=published_year,
            description=description
        )
        books_db.append(new_book)
        
        # Update author's books
        author.books.append(new_book)
        
        return new_book

schema = strawberry.Schema(query=Query, mutation=Mutation)
