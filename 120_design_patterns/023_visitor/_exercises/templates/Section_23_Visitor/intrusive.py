# c_ DoubleExpression
#     ___  -  value
#         ?  ?
#
#     ___ print  buffer
#         ?.ap.. st. v...
#
#     ___ eval r_ v...
#
#
# c_ AdditionExpression
#     ___  -  left right
#         ?  ?
#         ?  ?
#
#     ___ print buffer
#         ?.ap.. ('(')
#         l___.print ?
#         ?.ap.. ('+')
#         r___.print(?)
#         ?.ap.. (')')
#
#     ___ eval
#         r_ l____.ev.. + r___.ev..
#
#
# __ ________ __ _________
#     # represents 1+(2+3)
#     e = A...|
#         D... 1
#         A...|
#             D... 2
#             D... 3
#         |
#     |
#     buffer _     # list
#     ?.print ?
#     print(''.j.. ?  '=', ?.ev..
#
#     # breaks OCP: requires we modify the entire hierarchy
#     # what is more likely: new type or new operation?
