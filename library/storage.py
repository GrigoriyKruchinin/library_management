import os
import json
from typing import List

from library.book import Book


DATA_FILE = "library.json"


class Storage:
    """Класс для управления хранением данных в JSON файле."""

    @staticmethod
    def load_data() -> List[Book]:
        """Загружает данные из файла и возвращает список объектов Book."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        return []

    @staticmethod
    def save_data(books: List[Book]) -> None:
        """Сохраняет список объектов Book в файл."""
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(
                [book.to_dict() for book in books], file, ensure_ascii=False, indent=4
            )
