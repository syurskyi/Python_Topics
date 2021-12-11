#
#
# ______ l__
# ______ r__
# ______ _
# ______ t__
#
#
# c_ Counter
#
#     ___ -  start=0
#
#         lock _.?
#         value ?
#
#     ___ increment
#         l__.d..('wait  for lock')
#         l__.a..
#
#         ___
#             l__.d..('Acquire lock')
#             value  ?+1
#         ______
#             l__.r..
#
#
#
# ___ worker c
#
#     ___ i __ r.. 2
#
#         pause  r__.r__
#         l__.d..('sleeping @0.002f' ?
#         t__.s.. ?
#         ?.i..
#
#     l__.d..('Done')
#
#
# l__.?
#     ?_l__.D..
#     ?_ _threadName -10_  _ m.. _
#
#
#
# counter ?
# ___ i __ r.. 2
#     t _.? ?_?  ?_?
#     ?.s..
#
# l__.d.. 'Waiting for worker threads'
# main_thread  _.?
# ___ t __ _.e..
#     __ t __ n.. ?
#         ?.j..
# l__.d.. 'Counter: @', ?.v..
#
