#
# # threading_semaphore.py
#
# ______ l..
# ______ r..
# ______ t..
# ______ t..
#
#
# c_ ActivePool
#
#     ___ -
#         s.. ? ?. -
#         active _   # list
#         lock _ ?.L..
#
#     ___ makeActive name
#         w__ ?
#             a__.ap.. ?
#             l__.d.. 'Running: @' ?
#
#     ___ makeInactive name
#         w__ ?
#             a__.r.. ?
#             l__.d.. 'Running: @' ?
#
#
# ___ worker s pool
#     l__.d..('Waiting to join the pool')
#     w__ s
#         name _ ?.c_t.. .gN..
#         ?.mA.. ?
#         t__.s.. 0.1
#         ?.mI.. ?
#
#
# l__.b..?
#     l.._l__.D..
#     f.._'_|a..|_ |_|tN..|-2_| _|m..|_',
# )
#
# pool _ ?
# s _ ?.S.. 2
# ___ i __ ra.. 4
#     t _ ?.T..
#         t.._w..
#         n.._st. ?
#         a.._ ? p..
#     |
#     ?.s..
#
# # $ python3 threading_semaphore.py
# #
# # 2016-07-10 10:45:29,398 (0 ) Waiting to join the pool
# # 2016-07-10 10:45:29,398 (0 ) Running: ['0']
# # 2016-07-10 10:45:29,399 (1 ) Waiting to join the pool
# # 2016-07-10 10:45:29,399 (1 ) Running: ['0', '1']
# # 2016-07-10 10:45:29,399 (2 ) Waiting to join the pool
# # 2016-07-10 10:45:29,399 (3 ) Waiting to join the pool
# # 2016-07-10 10:45:29,501 (1 ) Running: ['0']
# # 2016-07-10 10:45:29,501 (0 ) Running: []
# # 2016-07-10 10:45:29,502 (3 ) Running: ['3']
# # 2016-07-10 10:45:29,502 (2 ) Running: ['3', '2']
# # 2016-07-10 10:45:29,607 (3 ) Running: ['2']
# # 2016-07-10 10:45:29,608 (2 ) Running: []
