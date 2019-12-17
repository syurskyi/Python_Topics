# # Coding Exceptions Classes
# c_ General ? p_
# c_ Specific1 ? p_
# c_ Specific2 ? p_
#
# ___ raiser0
#     X = G..         # Raise superclass instance
#     r... ?
#
# ___ raiser1
#     X = S.1        # Raise subclass instance
#     r___ ?
#
# ___ raiser2
#     X = S.2       # Raise different subclass instance
#     r_ X
#
# ___ func i_ _0 _1 _2
#     t__
#         f...
#     e___ G...       # Match General or any subclass of it
#         _______ __
#         print('caught:', ___.ex.. 0|
