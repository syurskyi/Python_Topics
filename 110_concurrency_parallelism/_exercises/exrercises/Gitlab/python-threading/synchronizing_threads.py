# ______ l__
# ______ _
# ______ t__
#
#
# ___ consumer cond
#     """wait for the condition and use the resource"""
#     l__.d..('Starting consumer thread')
#     w__ ?
#         ?.w..
#         l__.d..('Resource is available to consumer')
#
#
# ___ producer cond
#     """set up the resource to be used by the consumer"""
#     l__.d..('Starting producer thread')
#     w__ ?
#         l__.d..('Making resource available')
#         ?.n..
#
#
# l__.?
#     ?_l__.D..
#     ?_ _ a.. _ _ t.. -2_  _ m.. _
#
#
# condition  _.?
# c1  _.? ?_ c1 ?_?
#                        ?_?
# c2  _.? ?_ c2 ?_?
#                        ?_?
# p  _.? ?_ p ?_?
#                       ?_?
#
# ?.s..
# t__.s.. 0.2
# ?.s..
# t__.s.. 0.2
# ?.s..