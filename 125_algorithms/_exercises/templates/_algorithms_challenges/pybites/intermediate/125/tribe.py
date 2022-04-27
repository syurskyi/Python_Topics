# ____ c.. _______ C..
#
# ____ ___ _______ B..
# _______ ___
# _______ r__
#
# AMAZON "amazon.com"
# # static copy
# TIM_BLOG ('https://bites-data.s3.us-east-2.amazonaws.com/tribe-mentors-books.html')
# MIN_COUNT 3
#
#
# ___ load_page
#     """Download the blog html and return its decoded content"""
#     w__ r__.S.. __ session
#         r.. ?.g.. ? .c__.d.. utf-8
#
#
# ___ get_top_books content_ N..
#     """Make a BeautifulSoup object loading in content,
#        find all links that contain AMAZON, extract the book title
#        (stripping spacing characters), and count them.
#        Return a list of (title, count) tuples where
#        count is at least MIN_COUNT
#     """
#     __ content __ N..
#         ? ?
#
#     soup B.. ? html.parser
#
#     amazon_books    # list
#     ___ link __ ?.f.. "a"
#         __ "amazon" __ ?.g.. "href"
#             ?.a.. ?.g.. .s...s.. "\n"
#
#     amazon_books_counter C..
#     ___ book __ a..
#         ?.u.. ?
#
#     r.. key value ___ ? ? __ ?.i.. __ ? >_ M..
#
#
# __ _______ __ _______
#     print ?