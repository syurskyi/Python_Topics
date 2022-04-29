# _______ i___
#
# ____ c.. _______ c.. c..
#
# expected = '''10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# time is up
# '''
# expected_other_start_arg = '''13
# 12
# 11
# '''
# expected_other_start_arg += expected
#
#
# ___ test_countdown_for capfd
#     ?
#     out, _  ?.r..
#     ... ? __ e..
#
#
# ___ test_countdown_recursive capfd
#     ?
#     out, _  ?.r..
#     ... ? __ e..
#
#
# ___ test_test_countdown_recursive_different_start capfd
#     ? 13
#     out, _  ?.r..
#     ... ? __ e..
#
#
# ___ test_recursion_used
#     func ?
#     err = _* expecting ?. -n twice in your answer
#     ... i___.g.. ? .c.. ?. -n __ 2 ?