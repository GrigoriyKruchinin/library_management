import unittest

from library.book import Book
from library.library import Library
from library.storage import Storage


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Настройка тестовой среды перед запуском каждого теста."""
        self.library = Library()
        # Очищаем библиотеку перед каждым тестом
        self.library.books = []
        Storage.save_data(self.library.books)

    def tearDown(self):
        """Очистка после завершения теста."""
        self.library.books = []
        Storage.save_data(self.library.books)

    def test_add_book(self):
        """Тестируем добавление книги."""
        self.library.add_book("Название", "Автор", 2022)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Название")

    def test_remove_book(self):
        """Тестируем удаление книги."""
        book = Book("Название", "Автор", 2022, "test-id")
        self.library.books.append(book)
        Storage.save_data(self.library.books)
        self.library.remove_book("test-id")
        self.assertEqual(len(self.library.books), 0)

    def test_search_books_by_title(self):
        """Тестируем поиск книги по названию."""
        book = Book("Название", "Автор", 2022, "test-id")
        self.library.books.append(book)
        Storage.save_data(self.library.books)
        results = self.library.search_books("Название", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Название")

    def test_search_books_by_author(self):
        """Тестируем поиск книги по автору."""
        book = Book("Название", "Автор", 2022, "test-id")
        self.library.books.append(book)
        Storage.save_data(self.library.books)
        results = self.library.search_books("Автор", "author")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Автор")

    def test_search_books_by_year(self):
        """Тестируем поиск книги по году издания."""
        book = Book("Название", "Автор", 2022, "test-id")
        self.library.books.append(book)
        Storage.save_data(self.library.books)
        results = self.library.search_books("2022", "year")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].year, 2022)

    def test_update_book_status(self):
        """Тестируем изменение статуса книги."""
        book = Book("Название", "Автор", 2022, "test-id", "в наличии")
        self.library.books.append(book)
        Storage.save_data(self.library.books)
        self.library.update_book_status("test-id", "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_display_books(self):
        """Тестируем отображение всех книг."""
        book = Book("Название", "Автор", 2022, "test-id")
        self.library.books.append(book)
        Storage.save_data(self.library.books)
        self.library.display_books()
        # Проверим, что метод не вызывает ошибок
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
