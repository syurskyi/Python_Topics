# ___ concat(x, y
#     r_ '| |'.f..(x, y)
#
#
# ___ sum_3_elem(a, b, c
#     r_ a + b + c
#
#
# ___ multiply_3_elem(a, b, c
#     r_ a * b * c
#
#
# ___ test_concat
#     a_ concat(1, 2) __ '1 2'
#     a_ concat(10, 20) __ '10 20'
#
#
# ___ test_sum_3_elem(
#     a_ ._3_(0, 2, 3) __ 5
#     a_ ._3_(1, 2, 3) __ 6
#     a_ ._3_(1, 3, 7) __ 11
#
#
# ___ test_multiply_3_elem
#     a_ ._3_.(1, 2, 3) __ 6
#     a_ ._3_.(2, 3, 4) __ 24
#
#
# test_functions _ [
#     t._c.
#     t._s._3_e.
#     t._m._3_e.
# ]
#
# __ ______ __ ______
#     ___ func i_ t._f.
#         t__
#             f..
#         e____ E. a_ e
#             print('Failed: | => |: |'.f... f.. ty.. e, e
