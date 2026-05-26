from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: Optional[int]
    reviews: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert the Book to a plain dictionary (for saving to JSON)."""
        # TODO: Return a dict representation of this book.
        # Hint: use self.id, self.title, self.author, self.year, self.reviews
        pass

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """Create a Book from a plain dictionary (for loading from JSON)."""
        # TODO: Build and return a Book object from the dict.
        # Hint: use Book(id=data["id"], title=..., ...)
        pass
