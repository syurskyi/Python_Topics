# ____ c.. _______ O..
# ____ f.. _______ r..
#
# # NUMERALS = OrderedDict(((1000, 'M'), (500, 'D'), (100, 'C'),
# #                         (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')))
#
# NUMERALS {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
#             40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
#             400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
# NUMS l.. r.. l.. ?.k..
#
#
# ___ romanutil n i.. queue l..
#     '''utility function for romanize recursive implementation'''
#     print _*entering romanutil with ?_
#     print _* ?_
#     chars ''
#     remainder 0
#     __ n __ N..
#         chars ? ?
#         q__.a.. ?
#         remainder 0
#         r..
#
#     ___ k __ N..
#         __ ? < n
#             quotient n // k
#             remainder n % k
#             chars chars + N ? * q..
#             print _* ?_
#             q__.a.. ?
#             _____
#
#     __ r.. __ 0
#         r..
#     ____
#         ? ? ?
#
#
# ___ romanize decimal_number i..
#     """Takes a decimal number int and converts its Roman Numeral str"""
#
#     __ n.. isi.. ? i.. o. 4000 <_ ? <_ 0
#         r.. V...
#
#     roman    # list
#     ? ? ?
#     roman_string ''.j.. ?
#     r.. ?
