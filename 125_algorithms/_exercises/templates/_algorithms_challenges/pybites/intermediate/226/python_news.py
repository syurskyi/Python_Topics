# ____ c.. _______ n..
# _______ __
#
# ____ ___ _______ B..
# _______ r__
#
# # feed = https://news.python.sc/, to get predictable results we cached
# # first two pages - use these:
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html
#
# Entry n.. 'Entry', 'title points comments'
#
#
# ___ _create_soup_obj url
#     """Need utf-8 to properly parse emojis"""
#     resp r__.g.. ?
#     ?.e.. "utf-8"
#     r.. B.. ?.t.., "html.parser"
#
#
# ___ get_top_titles url top=5
#     """Parse the titles (class 'title') using the soup object.
#        Return a list of top (default = 5) titles ordered descending
#        by number of points and comments.
#     """
#     soup ? ?
#
#
#     entries    # list
#     rows ?.f.. "tr" id=T..
#
#
#     get_number l.... s i.. __.s.. _ \d+ ?.g..
#
#
#     ___ row __ r..
#         links ?.s.. 'span.title a'
#         title_text ? 0 .g.. s..=T..
#         link_text ''
#         __ l.. l.. > 1
#             link_text l.. 1 .g.. s..=T..
#             ? _* ?
#
#
#         title_text _* t.. l..
#
#
#         next_row r__.f.. 'tr'
#
#         points ?.s.. 'span.controls > span.smaller' .g..
#
#         points g.. ?
#
#
#
#         comments n__.s.. 'span.naturaltime a' .g.. s..=T..
#
#         comments g.. ?
#
#
#         entry ? t.. p.. c..
#         e__.a.. ?
#
#
#     e__.s.. r.._T..k.._l.... x ?.p.. ?.c..
#
#     r.. e.. |t..
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
