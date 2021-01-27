#
# ___ factorial_head n
#
#     # this is the base case - 0!=1
#     __ ? __ 0
#         r_ 1
#
#     # use recursion
#     result1 = ? ?-1
#
#     # we do some operations
#     result2 = ? * _1
#     r_ ?
#
#
# ___ factorial_tail n accumulator=1
#
#     __ ? __ 1
#         r_ a..
#
#     r_ ? ?-1 ? * a__
#
#
# print ? 4
