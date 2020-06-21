# # threading_lock.py
#
# ______ l..
# ______ r..
# ______ th..
# ______ ti..
#
#
# c_ Counter
#
#     ___ - start_0
#         lock _ ?.L..
#         value _ ?
#
#     ___ increment
#         ?.d.. 'Waiting for lock'
#         l__.a..
#         ___
#             ?.d.. 'Acquired lock'
#             v.. _ v.. + 1
#         f..
#             l__.r..
#
#
# ___ worker c
#     ___ i __ ra.. 2
#         pause _ ra__.ra..
#         ?.d.. 'Sleeping _0.02_' ?
#         t__.s.. ?
#         c.i..
#     ?.d.. 'Done'
#
#
# ?.b..|
#     l..l__.D..
#     f.._'|_|tN..|-10_| _|m..|_'
# |
#
# counter _ C..
# ___ i __ ra.. 2
#     t _ ?.T.. t.._w.. a.._ ?
#     ?.s..
#
# ?.d.. 'Waiting for worker threads'
# main_thread _ ?.m..
# ___ t __ ?.en..
#     __ t __ no. ?
#         ?.j..
# ?.d.. 'Counter: @', c__.v..  # digital
#
# # $ python3 threading_lock.py
# #
# # (Thread-1  ) Sleeping 0.18
# # (Thread-2  ) Sleeping 0.93
# # (MainThread) Waiting for worker threads
# # (Thread-1  ) Waiting for lock
# # (Thread-1  ) Acquired lock
# # (Thread-1  ) Sleeping 0.11
# # (Thread-1  ) Waiting for lock
# # (Thread-1  ) Acquired lock
# # (Thread-1  ) Done
# # (Thread-2  ) Waiting for lock
# # (Thread-2  ) Acquired lock
# # (Thread-2  ) Sleeping 0.81
# # (Thread-2  ) Waiting for lock
# # (Thread-2  ) Acquired lock
# # (Thread-2  ) Done
# # (MainThread) Counter: 4