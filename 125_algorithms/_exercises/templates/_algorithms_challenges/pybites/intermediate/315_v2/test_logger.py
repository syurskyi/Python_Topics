# _______ l___
#
# _______ p__
#
# ____ ? _______ ?
#
#
# ___ test_sum_numbers_function_works caplog
#     ... ? 2, 9, 4, 11, 6 __ 12
#
#
# ___ test_sum_numbers_logging caplog
#     ?.s.. l___.I.. l.._ app
#     ? l.. r.. 1 11
#     ... l.. c__.r.. __ 1
#     record ?.r.. 0
#     ... ?.m.. __ 'logger'
#     ...  r__n.. __ 'app'
#     ...  r__l.. __ 'INFO'
#     e.. 'Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> output: 30'
#     ...  r__m.. __ e..
#
#
# ___ test_sum_numbers_throws_exception caplog
#     ?.s.. l___.I.. l.._ app
#     w__ p__.r.. T..
#         ? 1, 'a', 2, 3
#     ... l.. c__.r.. __ 1
#     record ?.r.. 0
#     ...  r__l.. __ 'ERROR'
#     e.. "Bad inputs: [1, 'a', 2, 3]"
#     ...  r__m.. __ e..
#     ... ?.e__.s.. 'Traceback')
#     ... ?.e__.e..
#         ('TypeError: not all arguments converted during '
#          'string formatting'