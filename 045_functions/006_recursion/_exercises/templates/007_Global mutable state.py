# # Global mutable state
# current_number = 1
# accumulated_sum = 0
#
#
# ___ sum_recursive
#     g_ c..
#     g_ a..
#     # Base case
#     __ c.. __ 11:
#         r_ a..
#     # Recursive case
#     ____
#         a.. = a.. + c..
#         c.. = c.. + 1
#         r_ ?
#
# print ?
# # 55
