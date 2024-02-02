import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2


    def test_set_books_genre_(self):
        collector = BooksCollector()
        collector.books_genre = {'Оно': 'Ужасы'}
        collector.genre = ['Ужасы', 'Детектив']
        collector.set_book_genre('Оно', 'Детектив')
        assert collector.books_genre['Оно'] == 'Детектив'

    def test_get_book_genre_(self):
       collector3 = BooksCollector()
       collector3.books_genre = {'Оно':'Ужасы', 'Собака Баскервилей': 'Детектив', 'Солярис':'Фантастика'}
       assert collector3.get_book_genre('Оно') == 'Ужасы'
       assert collector3.get_book_genre('Солярис') == 'Фантастика'


    def test_get_books_genre(self):
        collector = BooksCollector()
        test_books_genre = {'Оно':'Ужасы', 'Собака Баскервилей': 'Детектив', 'Солярис':'Фантастика'}
        collector.books_genre = test_books_genre
        assert collector.books_genre == test_books_genre


    def test_get_books_for_children(self):
        collector = BooksCollector()
        test_books_genre = {'Оно':'Ужасы', 'Собака Баскервилей': 'Детектив','Малыш и Карлсон':'Мультфильмы'}
        collector.books_genre = test_books_genre
        collector.genre = ['Ужасы', 'Детектив', 'Фантастика','Мультфильмы']
        collector.genre_age_rating = ['Ужасы','Детектив']
        assert collector.get_books_for_children() == ['Малыш и Карлсон']


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        test_books_genre = {'Оно': 'Ужасы', 'Собака Баскервилей': 'Детектив', 'Солярис': 'Фантастика', 'Малыш и Карлсон': 'Мультфильмы'}
        collector.books_genre = test_books_genre
        collector.favorites = ['Оно', 'Солярис']
        collector.add_book_in_favorites('Собака Баскервилей')
        assert 'Собака Баскервилей' in collector.favorites

    #удаление из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.favorites = ['Оно', 'Собака Баскервилей', 'Солярис']
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.favorites


    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        test_favorites = ['Оно', 'Собака Баскервилей', 'Солярис']
        collector.favorites = test_favorites
        result = collector.get_list_of_favorites_books()
        assert test_favorites == result


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Оно': 'Ужасы', 'Дракула':'Ужасы', 'Собака Баскервилей': 'Детектив', 'Солярис': 'Фантастика', 'Малыш и Карлсон': 'Мультфильмы'}
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Дракула']


    @pytest.mark.parametrize('book_name', [
        (''),
        ('Приключения ручного тестировщика на курсе яндекса по изучению питона')
    ])
    def test_add_new_book_empty_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    @pytest.mark.parametrize('book_name', [
        ('Testtesttestttestetstettstetsttetsttstettsttetstetstte'),
        ('Приключения ручного тестировщика на курсе яндекса по изучению питона')
    ])
    def test_add_new_book_long_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre


