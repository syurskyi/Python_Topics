# # threading_local_defaults.py
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
#         l___.d.. 'No value yet'
#     ____
#         l___.d..('value_@' ?
#
#
# ___ worker data
#     ? ?
#     ?.v.. _ ra__.r_i.. 1 100
#     ? ?
#
#
# c_ MyLocal ?.l..
#
#     ___ - value
#         s__ . -
#         l___.d..('Initializing @' ?
#         ? ?
#
#
# l___.b..
#     l.._l__.D..
#     f.._'|_|tN..|-10_| _|m..|_'
# )
#
# local_data _ ? 1000
# ? ?
#
# ___ i __ ra.. 2
#     t _ ?.T.. t.._w.. a.._ l..
#     ?.s..
#
# # $ python3 threading_local_defaults.py
# #
# # (MainThread) Initializing <__main__.MyLocal object at
# # 0x101c6c288>
# # (MainThread) value_1000
# # (Thread-1  ) Initializing <__main__.MyLocal object at
# # 0x101c6c288>
# # (Thread-1  ) value_1000
# # (Thread-1  ) value_18
# # (Thread-2  ) Initializing <__main__.MyLocal object at
# # 0x101c6c288>
# # (Thread-2  ) value_1000
# # (Thread-2  ) value_77