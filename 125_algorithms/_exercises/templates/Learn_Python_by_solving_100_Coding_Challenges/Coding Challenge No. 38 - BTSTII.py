# Best Time to Buy and Sell Stock II
# Question: Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Solutions:


c_ Solution:
    # @param prices, a list of integer
    # @return an integer
    ___ maxProfit(, prices):
        maxProfit _ 0
        ___ index __ ra..(le.(prices)-1):
            __ prices[index+1] > prices[index]:
            # As long as we can earn money, do the transaction.
                maxProfit +_ prices[index+1] - prices[index]
        r_ maxProfit


Solution().maxProfit([1, 2, 3, 0, 2])