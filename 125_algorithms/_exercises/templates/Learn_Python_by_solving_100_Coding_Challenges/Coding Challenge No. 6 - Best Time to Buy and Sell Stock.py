# Best Time to Buy and Sell Stock with Cool Down
# Question: Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again). After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Solutions:

c_ Solution:
    ___ maxProfit(prices):
        size _ le.(prices)
        __ size < 2:
            r_ 0
        buys _ [N..] * size
        sells _ [N..] * size
        sells[0], sells[1] _ 0, ma.(0, prices[1] - prices[0])
        buys[0], buys[1] _ -prices[0], ma.(-prices[0], -prices[1])
        ___ x __ ra..(2, size):
            sells[x] _ ma.(sells[x - 1], buys[x - 1] + prices[x])
            buys[x] _ ma.(buys[x - 1], sells[x - 2] - prices[x])
        r_ sells[-1]


Solution.maxProfit([1, 2, 3, 0, 2])