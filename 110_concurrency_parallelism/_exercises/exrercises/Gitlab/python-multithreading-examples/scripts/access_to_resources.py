# ______ l__
# ______ r__
# ______ _
# ______ t__
#
# l__.? ?_l__.D..
#                     ?_ _threadName -10s  _ m.. _
#
#
# c_ Counter o..
#     ___ -  start=0
#         lock  _.?
#         value = ?
#     ___ increment
#         l__.d.. Waiting for lock
#         l__.a..
#         ___
#             l__.d.. Acquired lock
#             value  ? + 1
#         ______
#             l__.r..
#
# ___ worker c
#     ___ i __ r.. 2
#         pause  r__.r__
#         l__.d.. Sleeping _0.02_ ?
#         t__.s.. ?
#         c.i..
#     l__.d.. Done
#
# counter = ?
# ___ i __ r.. 2
#     t = _.? ?_?  ?_ c..
#     ?.s..
#
# l__.d..('Waiting for worker threads')
# main_thread = _.c..
# ___ t __ _.e..
#     __ t __ n.. ?
#         ?.j..
# l__.d.. Counter: _d, c__.v..
