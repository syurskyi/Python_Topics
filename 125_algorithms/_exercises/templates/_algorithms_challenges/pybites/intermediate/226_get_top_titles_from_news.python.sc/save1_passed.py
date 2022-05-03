# ____ c.. _______ n..
# ____ ___ _______ B..
# _______ r__
# _______ __
#
# # feed = https://news.python.sc/, to get predictable results we cached
# # first two pages - use these:
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html
#
# Entry n..('Entry', 'title points comments')
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
#     titles ?.f.. 'span', {'class': 'title'
#     title_list entry.g.. .s.. ___ ? __ ?
#     point_list    # list
#     comment_list    # list
#
#     ___ entry __ ?.f.. 'span' attrs={'class': 'smaller'}
#         e.. ?.g.. .s..
#         points __.s.. _ (\d*) ? ?
#         comments __.s.. _ (\d*) c.. e..
#         __ p..
#             p__.a.. i.. p__.g.. 1
#         __ c..
#             c__.a.. i.. c__.g.. 1
#
#     output    # list
#     ___ entry __ z.. t.. p.. c..
#         ?.a.. ? t.._? 0 p.._? 1 c.._? 2
#
#     r.. s.. ?  k.._l.... x ?.p.. ?.c.. r.._T.. |t..
