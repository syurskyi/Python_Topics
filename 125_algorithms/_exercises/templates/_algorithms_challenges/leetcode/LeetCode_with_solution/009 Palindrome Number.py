# """
# Determine whether an integer is a palindrome. Do this without extra space.
# """
# __author__ = 'Danyang'
#
#
# c_ Solution
#     ___ isPalindrome  x
#         """
#         Algorithm: int, compare lsb and msb
#         No extra space
#         If you are thinking of converting the integer to string, note the restriction of using extra space.
#
#         :param x: int
#         :return: boolean
#         """
#         __ x < 0
#             r.. F..
#
#         # find order of magnitude
#         div = 1
#         w.... x/? >_ 10
#             ? *_ 10  # without touch x
#
#         w.... ? > 0
#             msb  ?/?
#             lsb  ?%10
#
#             __ m.. !_ l..
#                 r.. F..
#
#             # shrink
#             ? %_ ?
#             ? /_ 10
#
#             ? /_ 100
#
#         r.. T..
#
#
# __ _______ __ _______
#     ?.i.. 2147483647