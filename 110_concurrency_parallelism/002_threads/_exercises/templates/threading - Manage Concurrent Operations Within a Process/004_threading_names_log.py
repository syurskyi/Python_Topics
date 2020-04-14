# # threading_names_log.py
#
# ______ l..
# ______ t..
# ______ t..
#
#
# ___ worker
#     l__.d.. 'Starting'
#     t__.s.. 0.2
#     l__.d..('Exiting')
#
#
# ___ my_service
#     l__.d..('Starting')
#     t__.s.. 0.3
#     l__.d..('Exiting')
#
#
# l__.bC..(
#     l.._l__.D..
#     f.._'|_|l..|_| |_|tN..|-10_| _|m..|_',
# )
#
# t _ ?.T.. n.._'my_service', t.._?
# w _ ?.T.. n.._'worker', t.._?
# w2 _ ?.T.. t.._?  # use default name
#
# w.s..
# w2.s..
# t.s..
#
# # $ python3 threading_names_log.py
# #
# # [DEBUG] (worker    ) Starting
# # [DEBUG] (Thread-1  ) Starting
# # [DEBUG] (my_service) Starting
# # [DEBUG] (worker    ) Exiting
# # [DEBUG] (Thread-1  ) Exiting
# # [DEBUG] (my_service) Exiting
