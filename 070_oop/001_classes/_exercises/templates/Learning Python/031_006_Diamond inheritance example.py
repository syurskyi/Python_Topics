#
# c_ A
#     attr = 1         # Classic (Python 2.6)
#
#
# c_ B A          # B and C both lead to A
#     p..
#
#
# c_ C A
#     attr = 2
#
#
# c_ D B C
#     p...             # Tries A before C
#
# x = D
# print(x.a..               # Searches x, D, B, A
#
#
# c_ A o..
#     attr = 1         # New-style ("object" not required in 3.0)
#
#
# c_ B A
#     p..
#
#
# c_ C A
#     attr = 2
#
#
# c_ D B C
#     p...             # Tries C before A
#
# x = D
# print ?.a..               # Searches x, D, B, C
#
#
