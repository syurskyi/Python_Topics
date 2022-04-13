# ____ c.. _______ n..
#
# ____ ___ _______ B.. __ S..
# _______ r__
#
# CONTENT r__.g.. 'http://bit.ly/2EN2Ntv' .t..
#
# Book n..('Book', 'title description image link')
#
#
# ___ get_book
#     """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
#     soup S.. ?
#     dotd ?.f.. id='deal-of-the-day'
#     image_base ?.f.. c.._'dotd-main-book-image'
#     title_base ?.f.. c.._'dotd-title'
#
#     title ?.f.. 'h2' .t__.s..
#     description ?.p__.f.. 'div' 2 .t__.s..
#     image ?.f.. 'img' .a.. 'src'
#     link ?.f.. 'a' .a.. 'href'
#
#     r.. ? ? ? ? ?
