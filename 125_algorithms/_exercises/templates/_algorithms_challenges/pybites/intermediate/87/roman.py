# ____ c.. _______ O..
#
# ____ a__.v.. _______ d..
#
#
# ___ romanize decimal_number
#     """Takes a decimal number int and converts its Roman Numeral str"""
#
#     numeral_lookup O..([(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")])
#
#     __ isi.. ? i..
#         __ ? <_ 0 o. ? >_ 4000
#             r.. V...
#     ____
#         r.. V...
#
#     ___
#         ? ?
#         r.. numeral
#     ______ E..
#         p..
#
#     roman_numeral ""
#     w.... ? !_ 0
#
#         __ ? > 1000
#             frequency i..? / 1000
#             ? ? % 1000
#             roman_numeral += f.. * n.. 1000
#         ____
#             ___ key __ s.. ?.k.. r.._T..
#                 __ ? > 4 a.. ? % ? __ 0
#                     r... +_ ? ?
#                     ? 0
#                     _____
#                 ____
#                     f.. ? / ?
#                     remainder ? % k..
#
#                     __ r.. __ ?
#                         _____
#                     ____
#                         __ f.. > 1
#                             r.. +_ i.. f.. * ? k..
#                         ____
#                             r.. +_ ? k..
#                         ? r..
#                         _____
#
#         __ ? > 0 a.. ? <_ 3
#             r.. +_ r.. * ? 1
#             ? 0
#
#     r.. r..
#
#
# __ _______ __ _______
#     print ? 87
#