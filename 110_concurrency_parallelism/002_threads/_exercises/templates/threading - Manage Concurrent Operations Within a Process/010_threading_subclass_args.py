# # threading_subclass_args.py
#
# ______ t..
# ______ l..
#
#
# c_ MyThreadWithArgs ?.T..
#
#     ___ - group_N.. target_N.. name_N..
#                  args_|| kwargs_N.. * daemon_N..
#         s__. - g.._g.. t.._t.. n.._n..
#                          d.._d..
#         a.. _ ?
#         k.. _ ?
#
#     ___ run
#         l__.d.. 'running with @ and @',
#                       a.. k..
#
#
# l__.b..|
#     l..?.D..
#     f.._'|_|tN..|-10_| _|m..|_',
# |
#
# ___ i __ ra.. 5
#     t _ ?(args_|?,|, kwargs_|'a': 'A', 'b': 'B'
#     t.s..
#
# # $ python3 threading_subclass_args.py
# #
# # (Thread-1  ) running with (0,) and {'b': 'B', 'a': 'A'}
# # (Thread-2  ) running with (1,) and {'b': 'B', 'a': 'A'}
# # (Thread-3  ) running with (2,) and {'b': 'B', 'a': 'A'}
# # (Thread-4  ) running with (3,) and {'b': 'B', 'a': 'A'}
# # (Thread-5  ) running with (4,) and {'b': 'B', 'a': 'A'}