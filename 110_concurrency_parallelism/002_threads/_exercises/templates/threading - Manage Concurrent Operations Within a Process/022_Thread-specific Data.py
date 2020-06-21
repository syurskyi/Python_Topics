# # threading_local.py
#
# ______ ra..
# ______ t..
# ______ l..
#
#
# ___ show_value data
#     ___
#         val _ ?.v..
#     ______ A..
#         l__.d.. 'No value yet'
#     ____
#         l__.d..('value=@' ?
#
#
# ___ worker data
#     s_v.. ?
#     ?.v.. _ ra__.r_i. 1 100
#     ? ?
#
#
# l__.b..
#     l.._l__.D..
#     f.._'|_|tN..-10_| _|m..|_'
#
#
# local_data _ ?.l..
# show_value ?
# ?.v.. _ 1000
# ? ?
#
# ___ i __ ra.. 2
#     t _ ?.T.. t.._w... a.._ l..
#     ?.s..
#
# # $ python3 threading_local.py
# #
# # (MainThread) No value yet
# # (MainThread) value=1000
# # (Thread-1  ) No value yet
# # (Thread-1  ) value=33
# # (Thread-2  ) No value yet
# # (Thread-2  ) value=74

