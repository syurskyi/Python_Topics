# ____ tw__.in.. ______ r.. d..
#
#
# ___ resolve_deferred deff value
#     ___
#         ?.ca.. ?
#     ______ E.. __ e
#         ?.e.. ?
#
#
# ___ make_data raw timeout
#     print('make data called')
#     deferred _ defer.D..  # Future()
#     r__.cL..|
#         t..
#         r..
#         d..
#         r..
#     )  # Future.set_result
#     r_ d..
#
#
# ___ pipe_1 result
#     print('Logging value: @'.f.. ?
#     r_ ?
#
#
# ___ pipe_2 result
#     r_ ? + 10
#
#
# ___ pipe_3 result
#     r_ ? * 2
#
#
# ___ pipe_4 result
#     r_ 100 / ?
#
#
# ___ error_1 e
#     print('Error: @'.f.. ?
#
#
# deferred _ make_data(40, 2)
# ?.aC.. p_1
# ?.aC.. p_2
# ?.aC.. p_1
# ?.aC.. p_3
# ?.aC.. p_1
# ?.aC.. p_4
# ?.aC..(pipe_1, error_1)
#
# deferred _ make_data(-10, 2)
# ?.aC... p_1
# ?.aC... p_2
# ?.aC... p_1
# ?.aC... p_3
# ?.aC... p_1
# ?.aC... p_4
# ?.aC..(pipe_1, error_1)
#
# r__.cL.. 4, r__.st..
#
# print('Reactor is starting.')
# r__.r..
# print('Reactor is stopped.')
