# c_ PriceRule
#     """PriceRule is a rule that triggers when a stock price satisfies a
#     condition (usually greater, equal or lesser than a given value)"""
#
#     ___  -  symbol, condition
#         ? ?
#         ? ?
#
#     ___ matches exchange
#         ___
#             stock _ ? s..
#         _____ K..
#             r_ F..
#         r_ c.. ? __ ?.p.. ____ F..
#
#     ___ depends_on
#         r_ |s..
#
#
# c_ AndRule
#     ___  -  $
#         rules _ ar..
#
#     ___ matches exchange
#         r_ al. ?.ma.. ? ___ rule __ ?
#
#     ___ depends_on
#         depends _ se.
#         ___ rule __ r..
#             depends _ ?.u.. r__.d_o.
#         r_
