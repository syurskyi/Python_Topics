# ___ getopts argv
#     opts =      # dict
#     w___ a..
#         __ a..|0 0 __ '-'                  # find "-name value" pairs
#             ?|a.. 0 _ a.. 1            # dict key is "-name" arg
#             a.. _ a.. 2:
#         ____
#             a.. _ a.. 1
#     r_ ?
#
# __ ______ __ _____
#     .... ___ ________ a..                       # example client code
#     myargs = ? a..
#     __ '-i' __ ?
#         print ? '-i'
#     print ?
#
# # C:\...\PP4E\System> python testargv2.py
# # {}
# # C:\...\PP4E\System> python testargv2.py -i data.txt -o results.txt
# # data.txt
# # {'-o': 'results.txt', '-i': 'data.txt'}
