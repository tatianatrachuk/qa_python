# qa_python
1. test_add_new_book_add_two_books - Тест на проверку добавления двух книг.
2. test_set_book_rating_set_rating_0 - Тест на выставление рейтинга меньше 1. В тесте задаем рейтинг 0, ожидаемый результат: выставится рейтинг 1.
3. test_set_book_rating_set_rating_11 - Тест на выставление рейтинга больше 10. В тесте задаем рейтинг 12, ожидаемый результат: выставится рейтинг 1.
4. test_add_new_book_add_the_same_book_twice - Тест на добавление одной и той же книги дважды.
5. test_set_book_rating_set_rating_when_books_not_in_list - Тест на выставление рейтинга книге, которой нет в списке.
6. test_get_books_with_specific_rating_7 - Тест на получение списка книг с определенным рейтингом.
7. test_get_books_with_specific_rating_when_books_not_in_list - Тест на проверку получения пустого списка книг по определенному рейтингу, если ни одна книга с эти рейтингом не добавлена в список
8. test_get_books_rating_get_rating_none_when_books_not_in_list - Тест на проверку, что у не добавленной книги нет рейтинга
9. test_add_book_in_favorites_add_two_books - Тест на проверку добавления книг в избранное
10. test_add_book_in_favorites_can_not_add_book_in_favorites_when_books_not_in_list - Тест на проверку, что нельзя добавить книгу в избранное, если она не добавлена в словарь books_rating
11. test_delete_book_from_favorites_delete_one_book - Тест на проврерку удаления книги из избранного