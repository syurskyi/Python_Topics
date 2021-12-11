# #!/usr/bin/python
#
#
# ______ l__
# ______ _
# ______ t__
#
# l__.? ?_l__.D..
#                     ?_ _threadName -10_  _ m.. _
#
#
# ___ lock_holder lock
#     l__.d.. Starting
#     w___ T..
#         l__.a..
#         ___
#             l__.d.. Holding
#             t__.s.. 0.5
#         ______
#             l__.d.. Not holding
#             l__.r..
#         t__.s.. 0.5
#     r_
#
# ___ worker lock
#     l__.d.. Starting
#     num_tries  0
#     num_acquires  0
#     w___ n.. < 3
#         t__.s.. 0.5
#         l__.d.. Trying to a..
#         have_it  l__.a.. 0
#         ___
#             n.. += 1
#             __ h..
#                 l__.d.. Iteration __: Acquired  n..
#                 n.. += 1
#             ____
#                 l__.d..('Iteration __: Not acquired' n..
#         ______
#             __ have_it
#                 l__.r..
#     l__.d.. 'Done after __ iterations' n..
#
#
# lock  _.?
#
# holder  _.? ?_?  ?_? ?_ LockHolder
# ?.s.. T..
# ?.s..
#
# worker  _.? ?_?  ?_? ?_ Worker
# ?.s..
