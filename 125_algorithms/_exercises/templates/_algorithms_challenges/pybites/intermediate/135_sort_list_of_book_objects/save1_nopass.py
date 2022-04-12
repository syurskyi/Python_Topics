____ c.. _______ n..
____ d__ _______ d__

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

___ sort_books_by_len_of_title(books=books
    name_list [entry.title ___ entry __ books]
    r.. m..(name_list, key=l..)


___ sort_books_by_first_authors_last_name(books=books
    author_list [entry.authors ___ entry __ books]
    f s..(author_list,
               k.._l.... x: x.s..(' ')[-1],
               r.._T..[0]
    r.. ''.j..([t.title
                    ___ t __ books
                    __ t.authors __ f])


___ sort_books_by_number_of_page(books=books
    page_list [entry.pages ___ entry __ books]
    r.. ''.j..([t.title
                    ___ t __ books
                    __ t.pages __ m..(page_list)])


___ sort_books_by_published_date(books=books
    date_list [d__.s..(entry.published, '_Y-%m-_d')
                 ___ entry __ books]
    l_pub s..(date_list, r.._T..[0]
    r.. ''.j..([t.title
                    ___ t __ books
                    __ t.published __ d__.s..(l_pub, '_Y-%m-_d')])