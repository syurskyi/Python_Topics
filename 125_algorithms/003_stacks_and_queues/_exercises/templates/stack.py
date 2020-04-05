# c_ Stack
#     ___ -
#         items _     # list
#
#     ___ push e
#         items _ |? + ?
#
#     ___ pop
#         r_ ?.p..
#
#
# s = ?
# ?.p..(5)  # [5]
# ?.p..(7)  # [7, 5]
# ?.p..(11)  # [11, 7, 5]
# print(s.pop())  # returns 11, left is [7, 5]
# print(s.pop())  # returns 7, left is [5]