# # Best Time to Buy and Sell Stock with Cool Down
# # Question: Say you have an array for which the ith element is the price of a given stock on day i.
# # Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and
# # sell one share of the stock multiple times) with the following restrictions:
# # You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# # After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# # Solutions:
#
# c_ Solution
#     ___ maxProfit prices
#         size _ le. ?
#         __ ? < 2
#             r_ 0
#         buys _ N.. * ?
#         sells _ N.. * ?
#         s.. 0 s.. 1 _ 0 ma. 0 ? 1 - ? 0
#         b.. 0 b.. 1 _ - ? 0 ma. - ? 0 - ? 1
#         ___ x __ ra.. 2 s..
#             s.. ? _ ma. s.. ? - 1 b.. ? - 1 + ? ?
#             b.. ? _ ma. b.. ? - 1 s.. ? - 2 - ? ?
#         r_ s.. -1
#
#
# ?.? 1, 2, 3, 0, 2