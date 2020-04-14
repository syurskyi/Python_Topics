# # threading_daemon_join.py
#
# ______ th..
# ______ ti..
# ______ l..
#
#
# ___ daemon
#     l__.d.. 'Starting'
#     t__.s.. 0.2
#     l__.d.. 'Exiting'
#
#
# ___ non_daemon
#     l__.d.. 'Starting'
#     l__.d.. 'Exiting'
#
#
# l__.b..|
#     l.._l__.D..
#     f.._'|_|tN..|-10_| _|m..|_'
# |
#
# d _ ?.T.. n.._'daemon', t.._d.. d.._T..
#
# t _ ?.T.. n.._'non-daemon' t.._n..
#
# d.s...
# t.s...
#
# d.j..
# t.j..
#
# # $ python3 threading_daemon_join.py
# #
# # (daemon    ) Starting
# # (non-daemon) Starting
# # (non-daemon) Exiting
# # (daemon    ) Exiting
#
