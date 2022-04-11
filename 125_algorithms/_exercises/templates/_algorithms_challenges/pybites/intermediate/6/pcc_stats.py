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
#     w__ o.. ? __ file
#         data  ?.r..
#
#         ___ row __ ?
#             current  ?.s.. "\n").s.. ","
#             __ ? 1  __ 'True'
#                 y.. ? 0 .l..
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
#
#     # your code
#     ___ row __ ?
#         challenge user  ?.s.. "/"
#         __ user __ ?
#             _____
#         ____
#             ?.u.. ?
#             ?.u.. ?
#
#     r.. S.. ?.m.. 0 0 ?.m.. 0 0 ?.m.. 0 1
#
#
# # if __name__ == "__main__":
# #     files=[
# #             "22/wonderfulboyx",
# #             "25/bbelderbos",  # ignored
# #             "25/clamytoe",
# #             "21/wonderfulboyx",
# #             "25/santiagobenitez",
# #             "23/santiagobenitez",
# #             "07/santiagobenitez"
# #         ]
# #     print(diehard_pybites(files))