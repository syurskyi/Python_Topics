# ______ u...
#
#
# ___ sum_two_values a b
#     r_ a + b
#
#
# ___ power x n
#     r_ x ** n
#
#
# ___ concat_values $
#     result _ ''
#     ___ item i_ a..
#         ? +_ st. i..
#     r_ ?
#
#
# ___ desc x y
#     i_ x __ 0
#         r____ V... ('`x` should not be equal 0')
#     r_ y / x
#
#
# c_ UtilsTestCase ?.?
#
#     ___ test_sum_two_values
#         value1 _ 10
#         value2 _ 20
#         result _ s..  _1 _2
#         a.E. r.. _1 + _2
#
#     ___ test_power
#         value _ 2
#         st _ 8
#         result _ p.. v.. st
#         expected_value _ value ** st
#         a.E. r.. e..
#
#     ___ test_concat_values
#         values _ 1, 2, 3, 4
#         result _ concat_values(*values
#         expected_result _ '1234'
#         a.E. r.. e..
#
#     ___ test_desc
#         x, y _ 10, 20
#         result _ desc(x, y)
#         expected_result _ y / x
#         a.E. r.. e..
#
#     ___ test_desc_with_zero
#         w___ a..R. V...
#             desc(0, 20)
