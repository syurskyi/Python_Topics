# # threading_timer.py
#
# ______ th..
# ______ ti..
# ______ l..
#
#
# ___ delayed
#     l__.d.. 'worker running'
#
#
# l__.b..|
#     l.._l__.D..
#     f.._'|_|tN..|-10_| _|m..|_'
# |
#
# t1 _ ?.T.. 0.3 ?
# t1.sN..('t1')
# t2 _ ?.T.. 0.3 ?
# t2.sN.. 't2'
#
# l__.d..('starting timers')
# t1.s..
# t2.s..
#
# l__.d..('waiting before canceling @', _2.gN..
# t__.s.. 0.2
# l__.d..('canceling @' _2.gN..
# t2.cancel()
# l__.d..('done')
#
# # $ python3 threading_timer.py
# #
# # (MainThread) starting timers
# # (MainThread) waiting before canceling t2
# # (MainThread) canceling t2
# # (MainThread) done
# # (t1        ) worker running
