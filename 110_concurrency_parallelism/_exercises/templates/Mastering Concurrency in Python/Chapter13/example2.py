# # ch13/example2.py
#
# ______ th..
#
# ___ writer
#     g.. text
#     g.. wcount
#
#     w__ T..
#         w__ wc..
#             ? +_ 1
#             __ ? __ 1
#                 r_t_.a..
#
#         w__ r..
#             print _*Writing being done by |?.c_t_ .n.. .')
#             t.. +_ f'Writing was done by |?.c_t_ .n.. . '
#
#         w__ wc..
#             ? -_ 1
#             __ ? __ 0
#                 r_t_.r..
#
# ___ reader
#     g.. rcount
#
#     w__ T..
#         w__ r_t..
#             w__ rc..
#                 ? +_ 1
#                 __ ? __ 1
#                     r__.a..
#
#             print _*Reading being done by |?.c_t__ .n.. :')
#             print t..
#
#             w__ rc..
#                 ? -_ 1
#                 __ ? __ 0
#                     r__.r..
#
# text _ 'This is some text. '
# wcount _ 0
# rcount _ 0
#
# wcounter _ ?.L..
# rcounter _ ?.L..
# resource _ ?.L..
# read_try _ ?.L..
#
# threads _ ?.T.. t_r.. ___ i __ ra.. 3||+ |?.T.. t.._w.. ___ i __ ra.. 2
#
# ___ thread __ ?
#     ?.s..
