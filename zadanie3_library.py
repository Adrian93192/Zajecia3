from typing import Dict, Optional

class Library:
    def __init__(self):
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

# Przykład użycia:
# lib = Library()
# lib.add_book("123", "Python 101")
# print(lib.find_book("123"))  # Python 101
# print(lib.find_book("000"))  # None
