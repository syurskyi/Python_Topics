# _______ p__
#
# ____ t.. _______ M..
#
#
# ?p__.f..
# ___ t10
#     r.. ? 10
#
#
# ?p__.f..
# ___ t3
#     r.. ? 3
#
#
# ?p__.m__.p. "arg, ret", [
#     (1, 1),
#     (5, 25),
#     (10, 100),
#     (100, 10000),
#
#
# ___ test_table_len arg ret
#     ... l.. ? ? __ ?
#
#
# ?p__.m__.p. "arg, ret", [
#     ((6, 6), 36),
#     ((4, 2), 8),
#     ((7, 6), 42),
#     ((8, 8), 64),
#     ((10, 10), 100),
#
# ___ test_calc t10 arg ret
#     ... t10.c.. $? __ ?
#
# ___ test_calc_exception t3 capfd
#     w__ p__.r.. I..
#         ?.c.. 3, 4
#     w__ p__.r.. I..
#         ?.c.. 4, 3
#
#
# ___ test_table_str t3
#     output s.. ?
#     ... '1 | 2 | 3' __ ?
#     ... '2 | 4 | 6' __ ?
#     ... '3 | 6 | 9' __ ?