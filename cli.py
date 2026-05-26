import click

from models import Book
from storage import load_books, save_books, next_id


@click.group()
def cli():
    """Book Catalog — manage your personal book collection."""
    pass


@cli.command()
@click.option("--title", required=True, help="Title of the book.")
@click.option("--author", required=True, help="Author of the book.")
@click.option("--year", type=int, default=None, help="Publication year (optional).")
def add(title: str, author: str, year: int):
    """Add a new book to the catalog."""
    # TODO:
    # 1. Load the current list of books with load_books().
    # 2. Create a new Book with the next available id (use next_id()).
    # 3. Append the new book to the list.
    # 4. Save the updated list with save_books().
    # 5. Print a confirmation message, e.g. "Added: <title> by <author> (id=<id>)".
    pass


@cli.command(name="list")
def list_books():
    """List all books in the catalog."""
    # TODO:
    # 1. Load the current list of books.
    # 2. If the list is empty, print "No books in your catalog." and return.
    # 3. Otherwise, print each book on one line.
    #    Suggested format: [id] Title — Author (Year)
    pass


@cli.command()
@click.argument("book_id", type=int)
def show(book_id: int):
    """Show details and reviews for a specific book."""
    # TODO:
    # 1. Load books and find the one with the matching id.
    # 2. If not found, print an error and return.
    # 3. Print the book's title, author, year, and each review.
    pass


@cli.command()
@click.argument("book_id", type=int)
def remove(book_id: int):
    """Remove a book from the catalog."""
    # TODO:
    # 1. Load books and find the one with the matching id.
    # 2. If not found, print an error and return.
    # 3. Remove the book from the list.
    # 4. Save the updated list.
    # 5. Print a confirmation message.
    pass


@cli.command()
@click.argument("book_id", type=int)
@click.argument("text")
def review(book_id: int, text: str):
    """Add a review to a book.

    Example: python main.py review 3 "Great read!"
    """
    # TODO:
    # 1. Load books and find the one with the matching id.
    # 2. If not found, print an error and return.
    # 3. Append the review text to book.reviews.
    # 4. Save the updated list.
    # 5. Print a confirmation message.
    pass
