# ____ c.. _______ C.., n..
# _______ __
# _______ u__.r..
#
# # prep
# tmp  __.g.. TMP  /tmp
# tempfile  __.p...j.. ? dirnames
# u__.r...u..
#     'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
#     ?
#
#
# IGNORE  'static templates data pybites bbelderbos hobojoe1848'.s..
#
# Stats  n..'Stats', 'user challenge'
#
#
# # code
#
# ___ gen_files tempfile ?
#
#
#     """
#     Parse the tempfile passed in, filtering out directory names
#     (first column) using the last "is_dir" column.
#
#     Lowercase these directory names and return them as a generator.
#
#     "tempfile" has the following format:
#     challenge<int>/file_or_dir<str>,is_dir<bool>
#
#     For example:
#     03/rss.xml,False
#     03/tags.html,False
#     03/Mridubhatnagar,True
#     03/aleksandarknezevic,True
#
#     => Here you would return 03/mridubhatnagar (lowercased!)
#        followed by 03/aleksandarknezevic
#     """
#
#     w__ o.. ? _ __ f
#         ___ line __ ?
#             name is_dir  ?.s.. ','
#             __ is_dir __ "True\n"
#                 y.. n__.l..
#
#
#
#
#
#
#
# ___ diehard_pybites files_ N..
#     """
#     Return a Stats namedtuple (defined above) that contains:
#     1. the user that made the most pull requests (ignoring the users in IGNORE), and
#     2. a tuple of:
#         ("most popular challenge id", "amount of pull requests for that challenge")
#
#     Calling this function on the default dirnames.txt should return:
#
#     Stats(user='clamytoe', challenge=('01', 7))
#     """
#     __ files __ N..
#         files  ?
#
#
#     users  C..
#     popular_challenges  C..
#
#     # your code
#
#     ___ file __ f..
#         challenge name  ?.s.. '/'
#         __ ? __ ?
#             _____
#         ? ? + 1
#         ? ? + 1
#
#
#     most_popular_user  u__.m.. 1 0 0
#     top_challenge  ?.m.. 1 0
#
#
#     r.. ? ? ?
#
#
#
#
#
#
#
#
