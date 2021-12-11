# ______ l__
# ______ _
# ______ t__
#
#
# ___ wait_for_event e
#     l__.d..('wait_for_event starting')
#     event_is_set  ?.w..
#     l__.d..('event set: @' ?
#
#
#
# ___ wait_for_event_timeout e t
#
#     w___ n.. ?.i..
#
#         l__.d..('wait_for_event_timeout starting')
#         event_is_set  ?.w.. ?
#         l__.d.. 'event set: @' ?
#
#         __ event_is_set
#             l__.d..('processing event')
#         ____
#             l__.d..('doing other work')
#
#
# l__.?
#     ?_l__.D..
#     ?_ _t.. -10_  _ m.. _
#
#
#
# e  _.?
#
# t1  _.? ?_ block ?_? ?_?
#
# ?.s..
#
#
# t2 _.? ?_ nonblock ?_? ?_ ? 2
#
# ?.s..
#
# l__.d..('Waiting before calling Event.set()')
# t__.s.. 0.3
# e.s..
# l__.d..('Event is set')