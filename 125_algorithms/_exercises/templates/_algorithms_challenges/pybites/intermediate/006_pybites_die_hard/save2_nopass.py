# ____ c.. _______ C.., n..
# _______ __
# _______ u__.r..
#
#
# tmp  __.g.. TMP  /tmp
# tempfile  __.p...j.. ? dirnames
# u__.r...u..
#     'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
#     ?
#
#
# IGNORE 'static templates data pybites bbelderbos hobojoe1848'.s..
#
# Stats n..('Stats', 'user challenge')
#
#
# ___ gen_files tempfile ?
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
#     file = o.. ?.r...l...s..
#
#     names    # list
#     ___ line __ ?
#         line  ?.s.. ',' 0
#         ?.a.. ?
#
#     filtered1  x ___ ? __ n.. __ "." n.. __ ?
#     exclude  item ___ ? __ ? ___ n.. __ I.. __ n.. __ ?
#
#     output  item ___ ? __ f.. __ i.. n.. __ ?
#
#     r.. ?
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
#     files  entry ___ ? __ ? __ ? n.. __ I...
#
#     stats_list    # list
#     challenge_list    # list
#     user_list    # list
#
#     ___ entry __ ?
#         entry  ?.s.. '/'
#         c__.a.. ? 0
#         u__.a.. ? 1
#
#     users  C.. ?
#     popular_challenges  C.. ?
#
#     ___ entry __ files
#         entry  ?.s.. '/'
#         ___ challenge number __ p_.i..
#             __ ? 0 __ ?
#                 s__.a.. ? u.._? 1 c.._ ? 0 ?
#
#     top_user  ?.m.. 1 0 0
#     top_challenge  p__.m.. 1 0
#     r.. stat ___ ? __ s..
#             __ ?.u.. __ t.. a.. ?.c.. __ ? 0