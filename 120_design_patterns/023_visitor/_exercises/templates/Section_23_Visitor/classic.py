# # taken from https://tavianator.com/the-visitor-pattern-in-python/
#
#
# ___ _qualname obj
#     """Get the fully-qualified name of an object (including module)."""
#     r_ ?. -m + '.' + ?.__qualname__
#
#
# ___ _declaring_class obj
#     """Get the name of the c_ that declared an object."""
#     name _ _q..  ?
#     r_ ? ;?.rf.. '.'
#
#
# # Stores the actual visitor methods
# _methods _     # dict
#
#
# # Delegating visitor implementation
# ___ _visitor_impl  arg
#     """Actual visitor method implementation."""
#     method _ _m... _q.. ty.. ____, ty.. a..
#     r_ ? ____ ?
#
#
# # The actual @visitor decorator
# ___ visitor arg_type
#     """Decorator that creates a visitor method."""
#
#     ___ decorator fn
#         declaring_class _ _d_c..?
#         _m... d_c.. a_t.. _ ?
#
#         # Replace all decorated methods with _visitor_impl
#         r_ _v_i..
#
#     r_ d...
#
#
# # ↑↑↑ LIBRARY CODE ↑↑↑
#
# c_ DoubleExpression
#     ___ - value
#         ?  ?
#
#     ___ accept visitor
#         ?.v... ?
#
#
# c_ AdditionExpression
#     ___ - left right
#         ?   ?
#         ?   ?
#
#     ___ accept visitor
#         ?.v.. ?
#
#
# c_ ExpressionPrinter:
#     ___ -
#         buffer _    # list
#
#     ?v.. D..
#     ___ visit  de
#         b__.ap.. st. ?.v..
#
#     ?v.. A..
#     ___ visit  ae
#         b___.ap.. ('(')
#         ?.l__.ac.. ?
#         b__.ap.. '+'
#         ?.r__.ac.. ?
#         b___.ap.. (')')
#
#     ___ -s
#         r_ ''.j.. b...
#
#
# __ ________ __ _________
#     # represents 1+(2+3)
#     e _ A..|
#         D.. 1,
#         A.. |
#             D... 2
#             D... 3
#         |
#     |
#     buffer _     # list
#     printer _ E..
#     ?.v.. ?
#     print ?
