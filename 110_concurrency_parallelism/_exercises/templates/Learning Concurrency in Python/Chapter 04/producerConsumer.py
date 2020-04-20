# ______ th..
# ______ ra..
# ______ ti..
#
# c_ Producer ?.T..
#     """
#     Produces random integers to a list
#     """
#
#     ___  -   integers condition
#         """
#         Constructor.
#
#         @param integers list of integers
#         @param condition condition synchronization object
#         """
#         ?.Thread. -
#         ? ?
#         ? ?
#
#     ___ run
#         """
#         Thread run method. Append random integers to the integers list
#         at random time.
#         """
#         w__ T..
#             integer _ ra__.r_i.. 0 256
#             c__.a..
#             print 'condition acquired by @'  n..
#             i__.ap.. i..
#             print '@ appended to list by @'  i.. n..
#             print 'condition notified by @'  n..
#             c__.n..
#             print 'condition released by @'  n..
#             c__.r..
#             t__.s.. 1
#
# c_ Consumer(?.T..
#     """
#     Consumes random integers from a list
#     """
#
#     ___  -  integers condition
#         """
#         Constructor.
#
#         @param integers list of integers
#         @param condition condition synchronization object
#         """
#         ?.Thread. -
#         ? ?
#         ? ?
#
#     ___ run
#         """
#         Thread run method. Consumes integers from list
#         """
#         w__ T..
#             c__.a..
#             print 'condition acquired by @'  n..
#             w__ T..
#                 __ i..
#                     integer _ i__.po.
#                     print '@ popped from list by @'  i... n..
#                     b..
#                 print 'condition wait by @'  n..
#                 c__.w..
#             print 'condition released by @'  n..
#             c__.r..
#
# ___ main
#     integers _   # list
#     condition _ ?.C..
#     t1 _ P.. i.. c..
#     t2 _ C.. i.. c..
#     t1.s..
#     t2.s..
#     t1.j..
#     t2.j..
#
# __ _________ __ ________
#     ?