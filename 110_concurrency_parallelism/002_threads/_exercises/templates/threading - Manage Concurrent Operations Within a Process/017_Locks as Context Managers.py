# # threading_lock_with.py
#
# ______ t..
# ______ l..
#
#
# ___ worker_with lock
#     w__ ?
#         l__.d.. 'Lock acquired via with'
#
#
# ___ worker_no_with lock
#     ?.a..
#     ___
#         l__.d.. 'Lock acquired directly'
#     f..
#         ?.r..
#
#
# l__.b..|
#     l.._l__.D..
#     f.._'|_|tN..|-10_| _|m..|_'
# )
#
# lock _ ?.L..
# w _ ?.T.. t.._w.. a.._ l..
# nw _ ?.T.. t.._w.. a.._ l..
#
# w.s..
# nw.s..
#
# # $ python3 threading_lock_with.py
# #
# # (Thread-1  ) Lock acquired via with
# # (Thread-2  ) Lock acquired directly