# _______ o..
#
# OPS '+': o__.a..
#        '-': o__.s..
#        '*': o__.m..
#        '/': o__.t..
#
#
# ___ simple_calculator calculation
#     """Receives 'calculation' and returns the calculated result,
#
#        Examples - input -> output:
#        '2 * 3' -> 6
#        '2 + 6' -> 8
#
#        Support +, -, * and /, use "true" division (so 2/3 is .66
#        rather than 0)
#
#        Make sure you convert both numbers to ints.
#        If bad data is passed in, raise a ValueError.
#     """
#     __ n.. a__ op __ ? ___ ? __ ?
#         r.. V...
#
#     # assume op is good and split the string
#     args ?.s..
#
#     __ l.. ? !_ 3
#         r.. V...
#
#     a, op, b args
#
#     # convert to int raising error. Note, int does this
#     a, b  i..(x) ___ ? __ ? ?
#
#     __ b __ 0 a.. o. __ '/'
#         r.. V...
#
#     r.. ? o. ? ?
