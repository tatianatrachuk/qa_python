from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_set_rating_0(self):

        rating = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        rating.add_new_book(name_book)
        rating.set_book_rating(name_book, 0)
        assert rating.get_book_rating(name_book) == 1

    def test_set_book_rating_set_rating_11(self):

        rating = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        rating.add_new_book(name_book)
        rating.set_book_rating(name_book, 11)
        assert rating.get_book_rating(name_book) == 1

    def test_add_new_book_add_the_same_book_twice(self):

        collector = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name_book)
        collector.add_new_book(name_book)
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating_when_books_not_in_list(self):

        rating = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        rating.set_book_rating(name_book, 5)
        assert rating.get_book_rating(name_book) != 5

    def test_get_books_with_specific_rating_7(self):

        rating = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        rating.add_new_book(name_book)
        rating.set_book_rating(name_book, 7)
        assert rating.get_books_with_specific_rating(7) == [name_book]

    def test_get_books_with_specific_rating_when_books_not_in_list(self):

        rating = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        rating.set_book_rating(name_book, 9)
        assert rating.get_books_with_specific_rating(9) == []

    def test_get_books_rating_get_rating_none_when_books_not_in_list(self):

        rating = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        rating.set_book_rating(name_book, 9)
        assert rating.get_book_rating(name_book) == None

    def test_add_book_in_favorites_add_two_books(self):

        favorite = BooksCollector()
        name_book = 'Гордость и предубеждение и зомби'
        name_book_2 = 'Что делать, если ваш кот хочет вас убить'
        favorite.add_new_book(name_book)
        favorite.add_new_book(name_book_2)
        favorite.add_book_in_favorites(name_book)
        favorite.add_book_in_favorites(name_book_2)
        assert len(favorite.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_can_not_add_book_in_favorites_when_books_not_in_list(self):

        favorite = BooksCollector()
        favorite.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert favorite.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_delete_one_book(self):
        favorite = BooksCollector()

        name_book = 'Гордость и предубеждение и зомби'
        favorite.add_new_book(name_book)
        favorite.add_book_in_favorites(name_book)
        favorite.delete_book_from_favorites(name_book)
        assert favorite.get_list_of_favorites_books() == []




