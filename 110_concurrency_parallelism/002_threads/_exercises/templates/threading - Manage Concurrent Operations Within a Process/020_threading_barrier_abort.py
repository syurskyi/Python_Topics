#
# # threading_barrier_abort.py
#
# ______ t..
# ______ t..
#
#
# ___ worker barrier
#     print ?.c_t.. .n..
#           'waiting for barrier with @ others'.f..
#               ?.n_w..
#     ___
#         worker_id _ ?.w..
#     ______ ?.BBE..
#         print(?.c_t.. .n.. 'aborting'
#     ____
#         print(?.c_t.. .n.. 'after barrier',
#               ?
#
#
# NUM_THREADS _ 3
#
# barrier _ ?.B.. ? + 1
#
# threads _ |
#     ?.T..|
#         n.._'worker-@' @ ?
#         t.._w..
#         a.._ b..
#     )
#     ___ i __ ra.. ?
# ]
#
# ___ t __ ?
#     print ?.n.. 'starting'
#     ?.s..
#     t__.s.. 0.1
#
# ?.a..
#
# ___ t __ ?
#     ?.j..
#
# # $ python3 threading_barrier_abort.py
# #
# # worker-0 starting
# # worker-0 waiting for barrier with 0 others
# # worker-1 starting
# # worker-1 waiting for barrier with 1 others
# # worker-2 starting
# # worker-2 waiting for barrier with 2 others
# # worker-0 aborting
# # worker-2 aborting
# # worker-1 aborting
