# ____ c.. _______ n..
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
#
#     soup S.. ? 'html.parser'
#     soup1 ?.f.. 'div' c.._'dotd-main-book-summary float-left'
#     soup2 ?.f.. 'div' c.._'dotd-main-book-image float-left'
#
#     title ?.f.. c.._'dotd-title' .s.. 'h2').-s
#     title ?.s.. '\t' 15
#
#     description ?.s.. 'div' 2 .-s
#     description ?.s.. '\t' 8
#
#     image ?.s.. 'img' 0 'src'
#
#     link ?.s.. 'a' 0 'href'
#
#     r.. ? t.._? d.._?
#                 i.._? l.._l..