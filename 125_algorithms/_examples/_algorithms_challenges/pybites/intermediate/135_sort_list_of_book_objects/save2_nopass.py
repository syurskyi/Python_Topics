from collections import namedtuple
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

def sort_books_by_len_of_title(books=books):
    return [entry.title for entry in books]


def sort_books_by_first_authors_last_name(books=books):
    f = sorted(books, key=attrgetter('authors'), reverse=True)
    return [b.title for b in f]


def sort_books_by_number_of_page(books=books):
    f = sorted(books, key=attrgetter('pages'))
    return [b.title for b in f]


def sort_books_by_published_date(books=books):
    f = sorted(books, key=attrgetter('published'))
    return [b.title for b in f]