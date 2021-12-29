from collections import namedtuple
from datetime import datetime
from operator import attrgetter

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

___ sort_books_by_len_of_title(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    len_of_title = sorted(books, key=lambda x: len(x.title))
    return len_of_title


___ sort_books_by_first_authors_last_name(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    first_authors_last_name = sorted(books, key=lambda book: len(book.authors.split(" ")[1].strip(" ")))
    return first_authors_last_name


___ sort_books_by_number_of_page(books=books):
    """
    Expected last book in list:
    Fluent Python
    """
    number_of_pages = sorted(books, key=lambda book: book.pages)
    return number_of_pages


___ sort_books_by_published_date(books=books):
    """
    Expected last book in list:
    Python Interviews
    """
    published_date = sorted(books, key=lambda book: book.published)
    return published_date
    


#if __name__ == "__main__":
     #sort_books_by_len_of_title()
     #sort_books_by_first_authors_last_name()
     #sort_books_by_published_date()