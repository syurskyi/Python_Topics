# _______ p__
#
# ____ wrong_char _______ get_index_different_char
#
#
# @p__.mark.parametrize("arg, expected", [
#     (['A', 'f', '.', 'Q', 2], 2),
#     (['.', '{', ' ^', '%', 'a'], 4),
#     ([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'], 1),
#     (['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'], 5),
#     (l..(r..(1, 9)) + ['}'] + l..('abcde'), 8),
#     ([2, '.', ',', '!'], 0),
# ])
# ___ test_wrong_char(arg, expected):
#     error = (f"get_index_different_char({arg}) should "
#              f"return index {expected}")
#     ... get_index_different_char(arg) __ expected, error