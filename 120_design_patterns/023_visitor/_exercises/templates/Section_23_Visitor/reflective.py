# ____ a.. ________ A..
#
#
# c_ Expression A..
#     p..
#
#
# c_ DoubleExpression E..
#     ___ - value
#         ?  ?
#
#
# c_ AdditionExpression E..
#     ___ - left right
#         ?  ?
#         ?  ?
#
#
# c_ ExpressionPrinter:
#     ??
#     ___ print e b..
#         """ Will fail silently on a missing case. """
#         __ isi... ? D..
#             b__.ap.. st. ?.v..
#         ____ isi... ? A..
#             b__.ap.. ('(')
#             Ex___.print ?.l.. b__
#             b__.ap.. ('+')
#             E___.print ?.r.. b__
#             b__.ap.. (')')
#
#     E___.print _ l____ ? b; EP__.print _____ ?
#
#
# # still breaks OCP because new types require M×N modifications
#
# __ ________ __ _________
#     # represents 1+(2+3)
#     e = A...|
#         D.. 1
#         A...|
#             D.. 2
#             D.. 3
#         |
#     |
#     buffer _    # list
#
#     # ExpressionPrinter.print(e, buffer)
#
#     # IDE might complain here
#     ?.print ?
#
#     print(''.j.. ?
