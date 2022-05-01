# _______ r__
# ____ ___ _______ B..
#
# cached_so_url 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'
#
#
# ___ top_python_questions url_?
#     """Use requests to retrieve the url / html,
#        parse the questions out of the html with BeautifulSoup,
#        filter them by >= 1m views ("..m views").
#        Return a list of (question, num_votes) tuples ordered
#        by num_votes descending (see tests for expected output).
#     """
#     response r__.g.. ?
#     soup B.. ?.t.., 'html.parser'
#     right_table ?.f.. 'div', {'class': 'question-summary'})
#
#     q    # list
#     vo    # list
#     vi    # list
#     ___ line __ ?
#         question ?.f.. 'a', {'class': 'question-hyperlink' .t..
#         vote ?.f.. 'span', {'class': 'vote-count-post high-scored-post'
#         view ?.f.. 'div', {'class': 'views supernova'
#
#         __ vote __ N..
#             ? 0
#         ____
#             v.. ?.t..
#
#         __ ? __ N..
#             v.. 0
#         ____
#             view ?.t__.s...s..  0
#
#         ?.a.. ?
#         ?.a.. ?
#         ?.a.. ?
#
#     vi_true    # list
#     ___ number __ vi
#         n.. s.. ?
#         __ ?.e.. 'k'
#             v__.a.. f__ n.. |-1  * 1000
#         __ ?.e.. 'm'
#             v__.a.. f__ n.. |-1 * 1_000_000
#         __ ? __ '0'
#             v__.a.. f__ ?
#
#     final l.. z.. ? ? ?
#     output1    # list
#     output2    # list
#     ___ question, vote, view __ f..
#         __ v.. >_ 1_000_000
#             o__.a.. ?
#             o__.a.. i.. v..
#
#     r.. s.. l.. z.. ? ? k.._l.... x ? 1 r.._T..