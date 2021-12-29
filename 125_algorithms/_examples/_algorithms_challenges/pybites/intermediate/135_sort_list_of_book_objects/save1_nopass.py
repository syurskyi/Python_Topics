from collections import namedtuple
from datetime import datetime

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
    name_list = [entry.title for entry in books]
    return max(name_list, key=len)


def sort_books_by_first_authors_last_name(books=books):
    author_list = [entry.authors for entry in books]
    f = sorted(author_list,
               key=lambda x: x.split(' ')[-1],
               reverse=True)[0]
    return ''.join([t.title
                    for t in books
                    if t.authors == f])


def sort_books_by_number_of_page(books=books):
    page_list = [entry.pages for entry in books]
    return ''.join([t.title
                    for t in books
                    if t.pages == max(page_list)])


def sort_books_by_published_date(books=books):
    date_list = [datetime.strptime(entry.published, '%Y-%m-%d')
                 for entry in books]
    l_pub = sorted(date_list, reverse=True)[0]
    return ''.join([t.title
                    for t in books
                    if t.published == datetime.strftime(l_pub, '%Y-%m-%d')])