from library.library import Library


def main():
    library = Library()

    while True:
        print("\n--- Система управления библиотекой ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отображение всех книг")
        print("5. Изменить статус книги")
        print("6. Выход\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)
        elif choice == "2":
            book_id = input("Введите ID книги, которую хотите удалить: ")
            library.remove_book(book_id)
        elif choice == "3":
            print("1. Поиск по названию")
            print("2. Поиск по автору")
            print("3. Поиск по году издания\n")
            search_choice = input("Выберите действие: ")
            query = input("Введите поисковый запрос: ")
            if search_choice == "1":
                results = library.search_books(query, "title")
            elif search_choice == "2":
                results = library.search_books(query, "author")
            elif search_choice == "3":
                results = library.search_books(query, "year")
            else:
                print("Неверный выбор.")
                continue

            if results:
                for book in results:
                    library.print_book(book)
            else:
                print("Книги не найдены.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = input("Введите ID книги: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            if new_status in ["в наличии", "выдана"]:
                library.update_book_status(book_id, new_status)
            else:
                print("Неверный статус.")
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
