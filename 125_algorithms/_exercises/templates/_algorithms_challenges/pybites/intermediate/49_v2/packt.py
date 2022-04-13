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
#
#
#     soup S.. ?"html.parser"
#
#     title ?.f.. 'div',c.._'dotd-title').g.. s..=T..
#     description ?.s.. 'div[class="dotd-main-book-summary float-left"] > div:nth-child(4)').g.. s..=T..
#
#     link ?.s.. 'div.dotd-main-book-image > a' 'href'
#     image ?.s.. 'div.dotd-main-book-image > a > img' 'data-original'
#
#
#     r.. ? ? ? ? ?
#
