# "collect command-line options in a dictionary"
#
# ___ getopts a..
#     opts _  # dict
#     w__ a..
#         __ a.. 0 0 __ '-':                 # find "-name value" pairs
#             ? a.. 0 _ a.. 1          # dict key is "-name" arg
#             a.. _ a.. 2|
#         ____
#             a.. _ a.. 1|
#     r_ ?
#
# __ _____ __ _____
#     ____ ___ ______ a..                       # example client code
#     myargs _ ? a..
#     __ '-i' __ ?
#         print ? '?'
#     print ?
