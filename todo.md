# Book Catalog — Implementation TODO

Work through the steps below in order. Each step builds on the previous one.
Run `python main.py --help` after each step to verify the CLI still works.

---

## Step 0 — Set up the environment

- [ ] Create and activate a virtual environment:
  ```
  python -m venv .venv
  source .venv/bin/activate        # macOS/Linux
  .venv\Scripts\activate           # Windows
  ```
- [ ] Install dependencies:
  ```
  pip install -r requirements.txt
  ```
- [ ] Verify the CLI loads without errors:
  ```
  python main.py --help
  ```

---

## Step 1 — Implement the `Book` model (`models.py`)

- [ ] Implement `Book.to_dict()` — return a plain `dict` with all fields.
- [ ] Implement `Book.from_dict()` — create a `Book` from a plain `dict`.
- [ ] Test manually in a Python shell:
  ```python
  from models import Book
  b = Book(id=1, title="1984", author="Orwell", year=1949)
  d = b.to_dict()
  print(d)
  b2 = Book.from_dict(d)
  print(b2)
  ```

---

## Step 2 — Implement storage (`storage.py`)

- [ ] Implement `load_books()` — read `books.json` and return a list of `Book` objects.
- [ ] Implement `save_books()` — write a list of `Book` objects to `books.json`.
- [ ] Implement `next_id()` — return the next available integer ID.
- [ ] Test: run `load_books()` when `books.json` does not exist; it should return `[]`.

---

## Step 3 — Implement `add` command (`cli.py`)

- [ ] Fill in the `add()` function so that running:
  ```
  python main.py add --title "1984" --author "Orwell" --year 1949
  ```
  adds the book and prints a confirmation.
- [ ] Check that `books.json` was created and contains the book.

---

## Step 4 — Implement `list` command (`cli.py`)

- [ ] Fill in `list_books()` so that running:
  ```
  python main.py list
  ```
  prints all books, or a friendly message when the catalog is empty.

---

## Step 5 — Implement `show` command (`cli.py`)

- [ ] Fill in `show()` so that running:
  ```
  python main.py show 1
  ```
  prints the book's details. Print an error if the id does not exist.

---

## Step 6 — Implement `remove` command (`cli.py`)

- [ ] Fill in `remove()` so that running:
  ```
  python main.py remove 1
  ```
  deletes the book and saves the updated list. Print an error if the id does not exist.

---

## Step 7 — Implement `review` command (`cli.py`)

- [ ] Fill in `review()` so that running:
  ```
  python main.py review 2 "Loved it!"
  ```
  appends the review to the book and saves. Print an error if the id does not exist.
- [ ] Verify that `show` now displays the reviews you added.

---

## Step 8 — End-to-end test

Run through this sequence manually to make sure everything works together:

- [ ] Add three books.
- [ ] List all books.
- [ ] Add two reviews to one book.
- [ ] Show that book and confirm the reviews appear.
- [ ] Remove one book.
- [ ] List again and confirm it is gone.

---

## Step 9 (Future) — Library book management

When you are ready to extend the application:

- [ ] Add a `borrowed` boolean and a `due_date` field to `Book`.
- [ ] Add a `borrow` command that marks a book as borrowed and sets a due date.
- [ ] Add a `return` command that marks it as returned.
- [ ] Add an `overdue` command that lists all books past their due date.
- [ ] Update `to_dict` / `from_dict` to handle the new fields.
