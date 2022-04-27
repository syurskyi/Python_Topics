# ____ c.. _______ n..
# ____ d__ _______ d__
# ____ o.. _______ a__
#
# Book n.. '?', 'title authors pages published'
#
# books
#     ?(title="Python Interviews",
#          authors="Michael Driscoll",
#          pages=366,
#          published="2018-02-28"),
#     ?(title="Python Cookbook",
#          authors="David Beazley, Brian K. Jones",
#          pages=706,
#          published="2013-05-10"),
#     ?(title="The Quick Python Book",
#          authors="Naomi Ceder",
#          pages=362,
#          published="2010-01-15"),
#     ?(title="Fluent Python",
#          authors="Luciano Ramalho",
#          pages=792,
#          published="2015-07-30"),
#     ?(title="Automate the Boring Stuff with Python",
#          authors="Al Sweigart",
#          pages=504,
#          published="2015-04-14"),
#
#
#
# # all functions return books sorted in ascending order.
#
# ___ sort_books_by_len_of_title books_?
#     """
#     Expected last book in list:
#     Automate the Boring Stuff with Python
#     """
#     r.. s.. ? k.._l.... x l.. ?.t..
#
#
# ___ _last_name book ?
#     r.. ?.a__.s.. ',' 0 .s.. ' ' -1
#
#
# ___ sort_books_by_first_authors_last_name books_?
#     """
#     Expected last book in list:
#     Automate the Boring Stuff with Python
#     """
#     r.. s.. ? key=_?
#
#
# ___ sort_books_by_number_of_page books_?
#     """
#     Expected last book in list:
#     Fluent Python
#     """
#     r.. s.. ? k.._l.... x ?.p..
#
#
# ___ sort_books_by_published_date books_?
#     """
#     Expected last book in list:
#     Python Interviews
#     """
#     r.. s.. ? k.._l.... x ?.p.. |4
