# # threading_lock_noblock.py
#
# ______ l..
# ______ t..
# ______ t..
#
#
# ___ lock_holder lock
#     l__.d.. 'Starting'
#     w__ T..
#         ?.a..
#         ___
#             l__.d..('Holding')
#             t__.s.. 0.5
#         f..
#             l__.d..('Not holding')
#             ?.r..
#         t__.s.. 0.5
#
#
# ___ worker lock
#     l__.d..('Starting')
#     num_tries _ 0
#     num_acquires _ 0
#     w__ _a.. < 3
#         t__.s.. 0.5
#         l__.d.. 'Trying to acquire'
#         have_it _ ?.a.. 0
#         ___
#             _t.. +_ 1
#             __ h_i.
#                 l__.d..('Iteration @: Acquired',
#                               _t..
#                 _a.. +_ 1
#             ____
#                 l__.d..('Iteration @: Not acquired'
#                               n_t..
#         f...
#             __ h_i.
#                 ?.r..
#     l__.d.. 'Done after @ iterations' _t..
#
#
# l__.b..|
#     l.._l__.D..
#     f.._'|_|tN..|-10_| _|m..|_'
# |
#
# lock _ ?.L..
#
# holder _ ?.T..|
#     t.._l..
#     a.._|l..,
#     n.._'LockHolder
#     d.._T..
# )
# ?.s..
#
# worker _ ?.T..|
#     t.._w..
#     a.._ l..
#     n.._'Worker',
# )
# ?.s..
#
# # $ python3 threading_lock_noblock.py
# #
# # (LockHolder) Starting
# # (LockHolder) Holding
# # (Worker    ) Starting
# # (LockHolder) Not holding
# # (Worker    ) Trying to acquire
# # (Worker    ) Iteration 1: Acquired
# # (LockHolder) Holding
# # (Worker    ) Trying to acquire
# # (Worker    ) Iteration 2: Not acquired
# # (LockHolder) Not holding
# # (Worker    ) Trying to acquire
# # (Worker    ) Iteration 3: Acquired
# # (LockHolder) Holding
# # (Worker    ) Trying to acquire
# # (Worker    ) Iteration 4: Not acquired
# # (LockHolder) Not holding
# # (Worker    ) Trying to acquire
# # (Worker    ) Iteration 5: Acquired
# # (Worker    ) Done after 5 iterations
