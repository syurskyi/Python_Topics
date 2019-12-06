# ___ getopts argv
# #     opts =      # dict
# #     w___ a..
# #         i_ a..  0 | 0 _ '-'                  # find "-name value" pairs
# #             ? | a.. 0 _ a.. 1            # dict key is "-name" arg
# #             a.. _ a.. 2:
# #         e__
# #             a.. _ a.. 1:
# #     r_ ?
# #
# # __ ______ __ _____
# #     f.. ___ ________ a..                       # example client code
# #     myargs = ? a..
# #     if '-i' i_ ?
# #         print ? '-i'
# #     print ?
# #
# # # C:\...\PP4E\System> python testargv2.py
# # # {}
# # # C:\...\PP4E\System> python testargv2.py -i data.txt -o results.txt
# # # data.txt
# # # {'-o': 'results.txt', '-i': 'data.txt'}