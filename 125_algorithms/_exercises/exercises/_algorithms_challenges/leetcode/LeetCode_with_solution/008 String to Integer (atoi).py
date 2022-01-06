# """
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
# what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather
# all the input requirements up front.
# """
# __author__ = 'Danyang'
#
#
# c_ Solution
#     ___ atoi  s..
#         """
#         Need to satisfy all the nuance requirements
#
#         :param str: string
#         :return: int
#         """
#         INT_MAX  2147483647
#         INT_MIN  -2147483648
#         # clean
#         s.. = s...s..
#         __ n.. s..:
#             r.. 0
#
#         # clean up leading sign
#         sign  1
#         __ s.. 0 __ "+", "-"
#             __ s.. 0 __ "-"
#                 sign _ -1
#             s.. _ s.. 1|
#
#         # check for leading digit
#         __ n.. s.. 0 .i..
#             r.. 0
#
#         # ignore the non-digit appended behind
#         # The string can contain additional characters after those that form the integral number,
#         # which are ignored and have no effect on the behavior of this function
#         ___ ind, val __ e.. s..  # find the 1st non-digit
#             __ n.. v__.i..
#                 s.. _ s.. |i..
#                 _____
#
#
#
#
#         # convert char array to integer
#         s..  0
#         scale  1
#         ___ element __ s.. ||-1
#             s.. += ?*i.. ?
#             ? *_ 10
#
#         # return sign*sum, and pay attention to the C constraints
#         result _ sign*s..
#         __ ? > I..
#             r.. I..
#         __ ? < I..
#             r.. I..
#         r.. ?
