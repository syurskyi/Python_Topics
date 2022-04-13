# ____ c.. _______ n..
#
# ____ ___ _______ B.. __ S..
# _______ r__
#
# PACKT 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
# CONTENT r__.g.. ? .t..
#
# Book n..('Book', 'title description image link')
#
#
# ___ get_book
#     """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
#     soup S.. ? "html.parser"
#
#     # Book title
#     book_title ?.f.. "div", c.._"dotd-title" 0.g.. .s..
#
#     # Book description
#     book_description ?.f.. "div", c.._"dotd-main-book-summary").s.. "div" 2 .g.. .s..
#
#     # Link
#     book_link  a "href" ___ ? __ ?.f.. "div", c.._"dotd-main-book-image" .s.. "a[href]" 0
#
#     # Image
#     book_image img "data-original" ___ ? __ ?.f.. "div", c.._"dotd-main-book-image" .s.. "img[data-original]" 0
#
#     # NamedTuple
#     book_nt ? ? ? ? ?
#     r.. ?
#
#
# # if __name__ == "__main__":
# #     get_book()