____ c.. _______ n..
____ d__ _______ d__
____ o.. _______ attrgetter

Book n..('Book', 'title authors pages published')

books [
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
    len_of_title s..(books, k.._l.... x: l..(x.title
    r.. len_of_title


___ sort_books_by_first_authors_last_name(books=books
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    first_authors_last_name s..(books, k.._l.... book: l..(book.authors.s..(" ")[1].s..(" ")))
    r.. first_authors_last_name


___ sort_books_by_number_of_page(books=books
    """
    Expected last book in list:
    Fluent Python
    """
    number_of_pages s..(books, k.._l.... book: book.pages)
    r.. number_of_pages


___ sort_books_by_published_date(books=books
    """
    Expected last book in list:
    Python Interviews
    """
    published_date s..(books, k.._l.... book: book.published)
    r.. published_date
    


#if __name__ == "__main__":
     #sort_books_by_len_of_title()
     #sort_books_by_first_authors_last_name()
     #sort_books_by_published_date()