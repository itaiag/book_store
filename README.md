# Book Catalog

A command-line tool for managing your personal book collection.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run all commands via `python main.py <command>`.

### Add a book

```bash
python main.py add --title "The Hobbit" --author "J.R.R. Tolkien" --year 1937
python main.py add --title "1984" --author "George Orwell"
```

`--year` is optional.

### List all books

```bash
python main.py list
```

Output format: `[id] Title — Author (Year)`

### Show book details

```bash
python main.py show 1
```

Displays title, author, year, and all reviews for the book with the given id.

### Add a review

```bash
python main.py review 1 "A timeless classic."
python main.py review 3 "Great read, highly recommended!"
```

### Remove a book

```bash
python main.py remove 2
```

### Help

```bash
python main.py --help
python main.py add --help
```
