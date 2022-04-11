____ books _______ (sort_books_by_len_of_title,
                   sort_books_by_first_authors_last_name,
                   sort_books_by_number_of_page,
                   sort_books_by_published_date)


___ test_sort_books_by_len_of_title
    last_book sort_books_by_len_of_title()[-1]
    ... last_book.title __ 'Automate the Boring Stuff with Python'


___ test_sort_books_by_first_authors_last_name
    last_book sort_books_by_first_authors_last_name()[-1]
    ... last_book.title __ 'Automate the Boring Stuff with Python'


___ test_sort_books_by_number_of_page
    last_book sort_books_by_number_of_page()[-1]
    ... last_book.title __ 'Fluent Python'


___ test_sort_books_by_published_date
    last_book sort_books_by_published_date()[-1]
    ... last_book.title __ 'Python Interviews'