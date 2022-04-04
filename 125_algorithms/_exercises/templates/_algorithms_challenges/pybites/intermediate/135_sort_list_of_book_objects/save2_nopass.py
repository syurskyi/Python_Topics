____ c.. _______ n..
____ o.. _______ attrgetter

Book = n..('Book', 'title authors pages published')

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

___ sort_books_by_len_of_title(books=books
    r.. [entry.title ___ entry __ books]


___ sort_books_by_first_authors_last_name(books=books
    f = s..(books, key=attrgetter('authors'), r.._T..
    r.. [b.title ___ b __ f]


___ sort_books_by_number_of_page(books=books
    f = s..(books, key=attrgetter('pages'
    r.. [b.title ___ b __ f]


___ sort_books_by_published_date(books=books
    f = s..(books, key=attrgetter('published'
    r.. [b.title ___ b __ f]