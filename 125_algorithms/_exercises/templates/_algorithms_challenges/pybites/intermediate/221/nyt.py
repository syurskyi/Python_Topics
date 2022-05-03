# _______ r__
#
# YOUR_KEY '123abc'
# DEFAULT_LIST 'hardcover-nonfiction'
#
# URL_NON_FICTION =  _*https://api.nytimes.com/svc/books/v3/lists/current/'
#                    _* D...json?api-key= Y..
# URL_FICTION URL_NON_FICTION.r..('nonfiction', 'fiction')
#
#
# ___ get_best_seller_titles url_?
#     """Use the NY Times Books API endpoint above to get the titles that are
#        on the best seller list for the longest time.
#
#        Return a list of (title, weeks_on_list) tuples, e.g. for the nonfiction:
#
#        [('BETWEEN THE WORLD AND ME', 86),
#         ('EDUCATED', 79),
#         ('BECOMING', 41),
#         ('THE SECOND MOUNTAIN', 18),
#          ... 11 more ...
#        ]
#
#        Dev docs: https://developer.nytimes.com/docs/books-product/1/overview
#     """
#     base_url 'https://api.nytimes.com/svc/books/v3'
#
#
#     url _*?/lists/hardcover-nonfiction.json"
#
#     params {'api-key': N..
#
#
#     books    # list
#     ___
#         response r__.g.. u.. p.._?
#         ?.r..
#     ______ r__.H.. __ e
#         print('HTTP Error')
#         print ?
#     ______ E.. __ e:
#         print('Other exception')
#         print ?
#     ____
#         results r__.j..
#
#
#         ___ book __ r.. 'results'  'books' :
#             ?.a.. ? 'title' ? 'weeks_on_list'
#         r.. ?
#
#
# __ _____ __ _____
#     ret ?
#     print ?
