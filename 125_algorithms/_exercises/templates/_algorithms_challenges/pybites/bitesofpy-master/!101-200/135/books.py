from collections ______ namedtuple
from datetime ______ datetime
from operator ______ attrgetter

Book = namedtuple('Book', 'title authors pages published')

books = [
    Book(title="Python Interviews",
         authors="Michael Driscoll",
         pages=366,
         published="2018-02-28"),
    Book(title="Python Cookbook",
         authors="David Beazley, Brian K. Jones",
         pages=706,
         published="2013-05-10"),
    Book(title="The Quick Python Book",
         authors="Naomi Ceder",
         pages=362,
         published="2010-01-15"),
    Book(title="Fluent Python",
         authors="Luciano Ramalho",
         pages=792,
         published="2015-07-30"),
    Book(title="Automate the Boring Stuff with Python",
         authors="Al Sweigart",
         pages=504,
         published="2015-04-14"),
]


# all functions return books sorted in ascending order.

___ sort_books_by_len_of_title(books=books
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    r_ sorted(books, key=lambda x: le.(x.title))


___ _last_name(book: Book
    r_ (book.authors.split(',')[0]).split(' ')[-1]


___ sort_books_by_first_authors_last_name(books=books
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    r_ sorted(books, key=_last_name)


___ sort_books_by_number_of_page(books=books
    """
    Expected last book in list:
    Fluent Python
    """
    r_ sorted(books, key=lambda x: x.pages)


___ sort_books_by_published_date(books=books
    """
    Expected last book in list:
    Python Interviews
    """
    r_ sorted(books, key=lambda x: x.published[:4])
