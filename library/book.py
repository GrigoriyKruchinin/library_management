from typing import Dict


class Book:
    """Класс, представляющий книгу в библиотеке."""

    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        book_id: str = None,
        status: str = "в наличии",
    ):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict[str, str]:
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Book":
        """Создает объект книги из словаря."""
        return cls(
            data["title"], data["author"], data["year"], data["id"], data["status"]
        )
