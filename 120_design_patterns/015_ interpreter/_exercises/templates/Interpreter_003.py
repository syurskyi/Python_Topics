# #_______________________________________________________________________________________________________________________
# ____ a.. ______ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Expression m..
#     """Abstract expression"""
#
#     ??
#     ___ interpreter var
#         p..
#
#
# c_ VarExpression E...
#     """Variable parser"""
#
#     ___ - key
#         __?  ?
#
#     ___ interpreter var
#         r_ ?.ge. __k..
#
#
# c_ SymbolExpression E..
#     """Operator parser, abstract class ___ operators"""
#
#     ___ - left right
#         _?  ?
#         _?  ?
#
#
# c_ AddExpression SE..
#     """Addition parser"""
#
#     ___ - left right
#         s___ . - ?  ?
#
#     ___ interpreter var
#         r_ _l___.int.. ? + _r___.int.. ?
#
#
# c_ SubExpression S..
#     """Subtraction parser"""
#
#     ___  - left right
#         s____. - left right
#
#     ___ interpreter var
#         r_ _l__.int.. ? - _r___.int.. ?
#
#
#
# c_ Stack
#     """Encapsulating a stack class"""
#
#     ___  -
#         items _    # list
#
#     ___ isEmpty
#         r_ le. i.. __ 0
#
#     ___ p..  item
#         i____.ap.. ?
#
#     ___ pop
#         r_ i___.p..
#
#     ___ peek
#         __ no iE..
#             r_ i___|le. i___| - 1
#
#     ___ size
#         r_ le. i___
#
#
# c_ Calculator
#     """Calculator"""
#
#     ___  -  text
#         __expression _ pT.. ?
#
#     ___ parserText expText
#         # Define a stack, processing sequence
#         stack _ S...
#         left _ right _ N.. # Left and right expression
#         idx _ 0
#         w___ id. < le. eT..
#             __ eT..|id. __ '+'
#                 left _ st__.po.
#                 id. +_ 1
#                 right _ VE... eT...|id.
#                 st__.p.. AE.. l.. r..
#             ____ eT..|id. __ '-'
#                 left _ st__.po.
#                 id. +_ 1
#                 right _ VE.. eT..|id.
#                 st__.pu.. SE.. l.. r..
#             ____
#                 st__.pu.. VE.. eT..|id.
#             id. +_ 1
#         r_ st__.po.
#
#     ___ run var
#         r_ __e_____.int.. ?
#
#
#
#
#
# # Version 2.0
# #_______________________________________________________________________________________________________________________
# # Code framework
# #______________________________
#
#
# # Framework-based implementation
# #______________________________
#
#
# # Test
# #_______________________________________________________________________________________________________________________
#
# ___ Stack
#     s _ S...
#     print ?.iE...
#     ?.p.. 4
#     ?.p.. 'dog'
#     print ?.pe..
#     ?.p.. T..
#     print ?.s..
#     print ?.iE...
#     ?.p.. 8.4
#     print ?.p..
#     print ?.p..
#     print ?.s..
#
#
#
# ___ Calculator
#     # Get expression
#     expStr _ in.. Please enter an expression
#     # Get the key-value pairs of each parameter
#     newExp, expressionMap _ gMV.. ?
#     calculator _ C.. n..
#     result _ ?.ru. eM...
#     print("The operation result is: " + eS.. + " _ " + st. ?
#
# ___ getMapValueexpStr
#     preIdx _ 0
#     expressionMap _    # dict
#     newExp _     # list
#     ___ i __ ra..  0 le. eS..
#         __ eS.. |? __ '+' or eS..|? __ '-
#             key _ eS.. |pI..;?
#             key _ ?.st..  # Remove leading and trailing blank characters
#             nE__.ap.. ?
#             nE__.ap.. eS.. |?
#             var _ in..("Please enter parameters" + k.. + "The value of ");
#             var _ ?.st..
#             eM..|k.. _ fl.. ?
#             preIdx _ ? + 1
#
#     # Processing the last parameter
#     key _ eS.. [pI..;le. eS..
#     key _ ?.st..  # Remove leading and trailing blank characters
#     nE__.ap.. ?
#     var _ in..("Please enter parameters" + k.. + "The value of: ");
#     var _ ?.st..
#     eM..|k.. _ fl.. ?
#
#     r_ nE.. eM..
#
#
# # testStack()
# Calculator()