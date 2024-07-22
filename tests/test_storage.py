import os
import unittest

from library.book import Book
from library.storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        """Настройка тестовой среды перед запуском каждого теста."""
        self.test_file = "test_library.json"
        Storage.DATA_FILE = self.test_file

    def tearDown(self):
        """Очистка после завершения теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_data_empty(self):
        """Тестируем загрузку данных из пустого файла."""
        books = Storage.load_data()
        self.assertEqual(books, [])

    def test_save_and_load_data(self):
        """Тестируем сохранение и загрузку данных."""
        book = Book("Название", "Автор", 2022, "test-id", "в наличии")
        Storage.save_data([book])
        books = Storage.load_data()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Название")
        self.assertEqual(books[0].author, "Автор")
        self.assertEqual(books[0].year, 2022)
        self.assertEqual(books[0].id, "test-id")
        self.assertEqual(books[0].status, "в наличии")


if __name__ == "__main__":
    unittest.main()
