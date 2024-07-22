import unittest

from library.book import Book


class TestBook(unittest.TestCase):
    def test_to_dict(self):
        """Тестируем метод to_dict."""
        book = Book("Название", "Автор", 2022, "test-id", "в наличии")
        book_dict = book.to_dict()
        expected_dict = {
            "id": "test-id",
            "title": "Название",
            "author": "Автор",
            "year": 2022,
            "status": "в наличии",
        }
        self.assertEqual(book_dict, expected_dict)

    def test_from_dict(self):
        """Тестируем метод from_dict."""
        book_dict = {
            "id": "test-id",
            "title": "Название",
            "author": "Автор",
            "year": 2022,
            "status": "в наличии",
        }
        book = Book.from_dict(book_dict)
        self.assertEqual(book.id, "test-id")
        self.assertEqual(book.title, "Название")
        self.assertEqual(book.author, "Автор")
        self.assertEqual(book.year, 2022)
        self.assertEqual(book.status, "в наличии")


if __name__ == "__main__":
    unittest.main()
