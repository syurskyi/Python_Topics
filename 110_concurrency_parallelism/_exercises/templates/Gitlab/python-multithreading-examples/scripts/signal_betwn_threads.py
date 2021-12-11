# ______ l__
# ______ _
# ______ t__
#
# l__.? ?_l__.D..
#                     ?_ _threadName -10_  _ m.. _
#
#
# ___ wait_for_event e
#     """Wait for the event to be set before doing anything"""
#     l__.d.. wait_for_event starting
#     event_is_set  ?.w..
#     l__.d..('event set: @' ?
#
# ___ wait_for_event_timeout e t
#     """Wait t seconds and then timeout"""
#     w___ n.. ?.i..
#         l__.d.. wait_for_event_timeout starting
#         event_is_set  ?.w.. ?
#         l__.d.. 'event set: @' ?
#         __ ?
#             l__.d..('processing event')
#         ____
#             l__.d..('doing other work')
#
#
# e  _.?
# t1  _.? ?_'block'
#                       ?_?
#                        ?_?
# ?.s..
#
# t2  _.? ?_'non-block'
#                       ?_?
#                        ?_? 2
# ?.s..
#
# l__.d..('Waiting before calling Event.set()')
# t__.s.. 3
# e.s..
# l__.d..('Event is set')
