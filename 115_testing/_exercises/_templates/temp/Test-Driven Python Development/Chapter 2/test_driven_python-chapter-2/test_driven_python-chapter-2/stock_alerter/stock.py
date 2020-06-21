# c_ Stock
#     ___  -  symbol
#         ? ?
#         price_history # list
#
#     ?p..
#     ___ price
#         r_ p..|-1 \
#             __ p.. ____ N..
#
#     ___ update timestamp price
#         __ ? < 0
#             r.. V..("price should not be negative")
#         p__.ap.. ?
#
#     ___ is_increasing_trend
#         r_ p..|-3 < \
#             p.. |-2 < p.. -1
