# Book Catalog using GraphQL
A sample Python project to explore GraphQL

 set up your environment:

```
poetry install
```

Run the server:

```
python main.py
```

Open your browser and go to http://localhost:8000/graphql to access the GraphQL playground.

Here are some example queries you can try:

```
# Get all books
query {
  books {
    id
    title
    publishedYear
    author {
      name
    }
  }
}

# Get a specific author and their books
query {
  author(id: 1) {
    name
    books {
      title
      publishedYear
    }
  }
}

# Add a new book
mutation {
  addBook(
    title: "New Book"
    authorId: 1
    publishedYear: 2024
    description: "A great new book"
  ) {
    id
    title
    author {
      name
    }
  }
}
```