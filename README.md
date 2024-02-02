Для тестирования приложения **BooksCollector** были созданы следующие юнит-тесты с использованием pytest.

1) `def test_add_new_book_add_two_books` тестирует метод def add_new_book(self, name), который добавляет новые книги.
Метод добавляет 2 книги и проверяет, что именно 2 добавились.
2) `def test_set_books_genre` проверяет установку жанра и есть ли жанр в списке жанров. 
3) `def test_get_book_genre` проверяет получение жанра книги по имени
4) `def test_get_books_genre` проверяет получение словаря 
5) `def test_get_books_for_children` проверяет, что в выдаче только детские книги
6) `def test_add_book_in_favorites` проверяет добавление книги в избранное
7) `def test_delete_book_from_favorites` проверяет удаление книги из избранного
8) `def test_get_list_of_favorites_books` проверяет получение списка избранных книг
9) `def test_get_books_with_specific_genre` проверяет списко книг по определенному жанру
10) тесты с параметризацией:
`def test_add_new_book_empty_name` проверяет, что книга с пустым названием не добавится в словарь
`def test_add_new_book_long_name` проверяет, что книга с длинным названием(более 40 символов) не добавится в словарь
