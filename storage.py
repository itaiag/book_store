import json
import os
from typing import List

from models import Book

DATA_FILE = "books.json"


def load_books() -> List[Book]:
    """Load all books from the JSON data file.

    Returns an empty list if the file does not exist yet.
    """
    # TODO: Check if DATA_FILE exists (hint: os.path.exists).
    # If it does not exist, return an empty list.
    # If it does, open the file, parse the JSON, and convert each
    # dict to a Book using Book.from_dict().
    pass


def save_books(books: List[Book]) -> None:
    """Save the list of books to the JSON data file."""
    # TODO: Convert each Book to a dict using book.to_dict().
    # Then write the resulting list to DATA_FILE as JSON.
    # Hint: use json.dump() with indent=2 for readable output.
    pass


def next_id(books: List[Book]) -> int:
    """Return the next available book ID."""
    # TODO: Find the maximum id among all books and return max + 1.
    # If there are no books, return 1.
    pass
