# ____ c.. _______ C.., n..
# ____ i.. _______ filterfalse
# _______ __
# _______ u__.r..
# _______ ___
# # prep
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
# # code
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
#     w__ o.. ? __ f lines  ?.r__.s..
#
#     filtered  f.. l.... x ?.s.. ',' -1__'True' ?
#     ___ line __ ?
#         y.. ?.s.. ',' 0 .l..
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
#     users  C..
#     popular_challenges  C..
#     files  l.. f.. l.... x ?.s.. '/' -1 __ ? ?
#     ?.u.. f.s.. '/' -1 ___ ? __ ?
#     ?.u.. f.s.. '/' 0 ___ ? __ ?
#     print l.. ? file=___.s.. flush_T..
#     r.. ? u.._?.m.. 1 0 0
#                  c.._ ?.m.. 1 0 0
#                             ?.m.. 1 0 1
#                  )
