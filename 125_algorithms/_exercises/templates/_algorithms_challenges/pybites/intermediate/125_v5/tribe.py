# ____ c.. _______ C..
#
# ____ ___ _______ B..
# _______ r__
#
# AMAZON "amazon.com"
# # static copy
# TIM_BLOG ('https://bites-data.s3.us-east-2.amazonaws.com/'
#             'tribe-mentors-books.html')
#
#
# ___ load_page
#     """Download the blog html and return its decoded content"""
#     w__ r__.S.. __ session
#         r.. ?.g.. ? .c__.d.. utf-8
#
#
# ___ get_top_books content_N.. limit=5
#     """Make a BeautifulSoup object loading in content,
#        find all links and filter on AMAZON, extract the book title
#        and count them, return the top "limit" books (default 5)"""
#     __ ? __ N..
#         ? ?
#     soup B.. ?
#     entry_content ?.f.. 'div', c.._'entry-content'
#     count C.. link.t.. ___ ? __ ?.s.. 'p > a' __ A.. __ ?.g.. 'href'
#     r.. title ___ ? _ __ ?.m.. l..
