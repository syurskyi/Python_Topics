# Best Time to Buy and Sell Stock IV
# Question: Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Solutions:

class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    ___ maxProfit(self, k, prices):
        __ prices is None or le.(prices) <_ 1 or k <_ 0:
            r_ 0
        n _ le.(prices)
        # k >= prices.length / 2 ==> multiple transactions Stock II
        __ k >_ n / 2:
            profit_max _ 0
            ___ i __ ra..(1, n):
                diff _ prices[i] - prices[i - 1]
                __ diff > 0:
                    profit_max +_ diff
            r_ profit_max

        f _ [[0 ___ i __ ra..(k + 1)] ___ j __ ra..(n + 1)]
        ___ j __ ra..(1, k + 1):
            ___ i __ ra..(1, n + 1):
                ___ x __ ra..(0, i + 1):
                    f[i][j] _ ma.(f[i][j], f[x][j - 1] + self.profit(prices, x + 1, i))
        r_ f[n][k]

        # calculate the profit of prices(l, u)
        ___ profit(self, prices, l, u):
            __ l >_ u:
                r_ 0
            valley _ 2**31 - 1
            profit_max _ 0
        ___ price __ prices[l - 1:u]:
            profit_max _ ma.(profit_max, price - valley)
            valley _ min(valley, price)
        r_ profit_max


Solution().maxProfit(8,[1, 4, 8, 1, 2, 10, 20, 30, 5, 3])