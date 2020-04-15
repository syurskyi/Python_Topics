# # threading_event.py
#
# ______ l..
# ______ th..
# ______ ti..
#
#
# ___ wait_for_event e
#     """Wait for the event to be set before doing anything"""
#     l__.d.. 'wait_for_event starting'
#     event_is_set _ ?.w..
#     l__.d..('event set: @' ?
#
#
# ___ wait_for_event_timeout e t
#     """Wait t seconds and then timeout"""
#     w__ no. ?.i_s..
#         l__.d.. 'wait_for_event_timeout starting'
#         event_is_set _ ?.w.. ?
#         l__.d.. 'event set: @' ?
#         __ ?
#             l__.d.. 'processing event'
#         ____
#             l__.d..('doing other work')
#
#
# l__.b..|
#     l.._l__.D..
#     f.._'|_|tN..|-10_| _|m..|_',
# )
#
# e _ ?.E..
# t1 _ ?.T..|
#     n.._'block',
#     t.._?
#     a.._?,
# )
# t1.s..
#
# t2 _ ?.T..|
#     n.._'nonblock',
#     t.._?
#     a.._? 2
# )
# t2.s..
#
# l__.d..('Waiting before calling Event.set()')
# t__.s.. 0.3
# e.s..
# l__.d..('Event is set')
#
# # $ python3 threading_event.py
# #
# # (block     ) wait_for_event starting
# # (nonblock  ) wait_for_event_timeout starting
# # (MainThread) Waiting before calling Event.set()
# # (MainThread) Event is set
# # (nonblock  ) event set: True
# # (nonblock  ) processing event
# # (block     ) event set: True
