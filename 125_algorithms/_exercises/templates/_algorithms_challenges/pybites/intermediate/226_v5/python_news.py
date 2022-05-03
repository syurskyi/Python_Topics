# _______ __
# ____ c.. _______ n..
#
# _______ r__
# ____ ___ _______ B..
#
# # feed = https://news.python.sc/, to get predictable results we cached
# # first two pages - use these:
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html
#
# Entry n.. 'Entry', 'title points comments'
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
#     article_list ?.s.. 'span.title'
#
#     articles    # list
#     ___ article __ a..
#         # Nasty hack, knowing the structure of the page:
#         stats ?.parent.parent.parent.next_sibling.next_sibling.text
#         # Get the number of points and comments, but don't check for plurals… just in case!
#         extract __.s.. _ (\d+) p__.* (\d+) c.. s.. __.D..
#         a__.a.. ? a__.t__.s.. i.. ?.g.. 1 i.. ?.g.. 2
#
#     r.. s.. a.. k.._l.... x - ?.p.. + ?.c.. / 1000 |t..
