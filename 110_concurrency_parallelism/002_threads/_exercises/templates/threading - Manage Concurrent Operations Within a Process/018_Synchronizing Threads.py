# # threading_condition.py
#
# ______ l..
# ______ t..
# ______ t..
#
#
# ___ consumer cond
#     """wait for the condition and use the resource"""
#     l__.d.. 'Starting consumer thread'
#     w__ ?
#         ?.w..
#         l__.d.. 'Resource is available to consumer'
#
#
# ___ producer cond
#     """set up the resource to be used by the consumer"""
#     l__.d.. 'Starting producer thread'
#     w__ ?
#         l__.d..('Making resource available')
#         ?.nA..
#
#
# l__.b..|
#     l.._l__.D..
#     f.._'_|a..|_ |_|tN..| -2_| _|m..|_',
# )
#
# condition _ ?.C..
# c1 _ ?.T..(n.._'c1' t.._c..
#                       a.._ c..
# c2 _ ?.T..(n.._'c2' t.._c..
#                       a.._ c..
# p _ ?.T..(n.._'p' t.._p..
#                      a.._ c..
#
# c1.s..
# t__.s.. 0.2
# c2.s..
# t__.s.. 0.2
# p.start()
#
# # $ python3 threading_condition.py
# #
# # 2016-07-10 10:45:28,170 (c1) Starting consumer thread
# # 2016-07-10 10:45:28,376 (c2) Starting consumer thread
# # 2016-07-10 10:45:28,581 (p ) Starting producer thread
# # 2016-07-10 10:45:28,581 (p ) Making resource available
# # 2016-07-10 10:45:28,582 (c1) Resource is available to consumer
# # 2016-07-10 10:45:28,582 (c2) Resource is available to consumer