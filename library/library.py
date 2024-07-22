import uuid
from typing import List

from library.book import Book
from library.storage import Storage


class Library:
    """Класс для управления библиотекой книг."""

    def __init__(self):
        self.books = Storage.load_data()

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет книгу в библиотеку."""
        new_book = Book(title, author, year, str(uuid.uuid4()))
        self.books.append(new_book)
        Storage.save_data(self.books)
        print("Книга успешно добавлена!")

    def remove_book(self, book_id: str) -> None:
        """Удаляет книгу из библиотеки по ID."""
        self.books = [book for book in self.books if book.id != book_id]
        Storage.save_data(self.books)
        print("Книга успешно удалена!")

    def search_books(self, query: str, key: str) -> List[Book]:
        """Ищет книги в библиотеке по заданному ключу."""
        if key == "year":
            return [book for book in self.books if str(book.year) == query]
        else:
            return [
                book
                for book in self.books
                if query.lower() in getattr(book, key).lower()
            ]

    def display_books(self) -> None:
        """Отображает все книги в библиотеке."""
        if self.books:
            for book in self.books:
                self.print_book(book)
        else:
            print("Библиотека пуста.")

    def update_book_status(self, book_id: str, new_status: str) -> None:
        """Изменяет статус книги по ID."""
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                Storage.save_data(self.books)
                print("Статус книги успешно обновлен!")
                return
        print("Книга не найдена.")

    @staticmethod
    def print_book(book: Book) -> None:
        """Выводит информацию о книге."""
        print(
            f"ID: {book.id}\nНазвание: {book.title}\nАвтор: {book.author}\n"
            f"Год издания: {book.year}\nСтатус: {book.status}\n"
        )
