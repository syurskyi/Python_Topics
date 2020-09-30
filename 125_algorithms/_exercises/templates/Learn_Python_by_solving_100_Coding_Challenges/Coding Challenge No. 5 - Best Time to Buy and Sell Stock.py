# Best time to buy and sell stock
# Question: Say you have an list for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Solutions:

class Solution:
    ___ maxProfit(prices):
        minValue = float("inf")
        maxBenefit = 0
        ___ price __ prices:
            if minValue > price:
                minValue = price
            if maxBenefit < price - minValue:
                maxBenefit = price - minValue
        r_ maxBenefit

print (Solution.maxProfit([7, 1, 5, 3, 6, 4]) )
print (Solution.maxProfit([7, 6, 4, 3, 1]) )