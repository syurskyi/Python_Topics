# # Best Time to Buy and Sell Stock IV
# # Question: Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most k transactions.
# # Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# # Solutions:
#
# c_ Solution
#     """
#     @param k: an integer
#     @param prices: a list of integer
#     @return: an integer which is maximum profit
#     """
#     ___ maxProfit k prices
#         __ ? __ N.. o. le. ? <_ 1 o. k <_ 0
#             r_ 0
#         n _ le. ?
#         # k >= prices.length / 2 ==> multiple transactions Stock II
#         __ k >_ n / 2
#             profit_max _ 0
#             ___ i __ ra.. 1 ?
#                 diff _ ? ? - ? ? - 1
#                 __ ? > 0
#                     p.. +_ d..
#             r_ ?
#
#         f _ 0 ___ i __ ra.. ? + 1 ___ j __ ra.. ? + 1
#         ___ j __ ra.. 1, ? + 1
#             ___ i __ ra.. 1 ? + 1
#                 ___ x __ ra.. 0 ? + 1
#                     ? ? ? _ ma. ? ? ? ? ? ? - 1 + p.. ? x + 1 ?
#         r_ ? ? ?
#
#         # calculate the profit of prices(l, u)
#         ___ p.. ? l u
#             __ l >_ u
#                 r_ 0
#             valley _ 2**31 - 1
#             profit_max _ 0
#         ___ price __ ? l - 1:u
#             profit_max _ ma. ? p.. - v..
#             valley _ mi. v.. p..
#         r_ ?
#
#
# ? .? 8,[1, 4, 8, 1, 2, 10, 20, 30, 5, 3]