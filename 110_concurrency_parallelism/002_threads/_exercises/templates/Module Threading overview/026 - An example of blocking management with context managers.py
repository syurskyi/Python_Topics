# _____ _
#
# ___ worker_with lock
#     w__ ?
#         th_name  _.c...n..
#         print _* ?: блокировка ставится через `with`
#
# ___ worker_finally lock
#     ?.a...
#     ___
#         th_name  _.c...n..
#         print _* ?: блокировка ставится явно
#     ______
#         ?.r...
#
#
# lock  _.?
#
# wh  _.? t.. ? a.. ?
# fin  _.? t.. ? a.. ?
#
# ?.s..
# ?.s..
#
# # Thread-1: блокировка ставится через `with`
# # Thread-2: блокировка ставится явно