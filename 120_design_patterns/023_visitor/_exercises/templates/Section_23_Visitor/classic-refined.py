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
#     name _ _q.. ?
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
#     method _ _m___ _q... ty.. ? ty.. a..
#     r_ ?  ? a..
#
#
# # The actual @visitor decorator
# ___ visitor arg_type
#     """Decorator that creates a visitor method."""
#
#     ___ decorator fn
#         declaring_class _ _d.. ?
#         _m___ d_c.. a_t.. _ ?
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
#     ___ accept  visitor
#         v___.v.. ?
#
#
# c_ AdditionExpression
#     ___ - left right
#         ?  ?
#         ?  ?
#
#     ___ accept  visitor
#         v___.v.. ?
#
#
# c_ ExpressionPrinter
#     ___ -
#         b.. _    # list
#
#     ?v.. D..
#     ___ visit de
#         b____.ap.. st. ?.v...
#
#     ?v.. A..
#     ___ visit  ae
#         b___.ap..('(')
#         ?.l___.ac... ?
#         b___.ap..('+')
#         ?.r___.ac... ?
#         b___.ap..(')')
#
#     ___ -s
#         r_ ''.j... b___
#
# c_ ExpressionEvaluator
#   ___ -
#     value _ N...
#
#    ?v.. D..
#   ___ visit  de
#     value _ ?.v...
#
#   ?v.. A..
#   ___ visit  ae
#     # ae.left.accept(self)
#     v.. ?.l..
#     temp _ value
#     # ae.right.accept(self)
#     vi... ?.r....
#     va.. +_ t...
#
#
# __ ________ __ _________
#     # represents 1+(2+3)
#     e _ A....|
#         D... 1
#         A....(
#             D... 2
#             D... 3
#         |
#     |
#     printer _ E...
#     ?.v.. ?
#
#     evaluator _ E...
#     ?.v.. ?
#
#     print _*|p... _ |e___.v...
