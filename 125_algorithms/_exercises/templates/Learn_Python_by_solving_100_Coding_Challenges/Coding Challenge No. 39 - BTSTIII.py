# Best Time to Buy and Sell Stock III
# Question: Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Solutions:


class Solution:
    # @param prices, a list of integer
    # @return an integer
    ___ maxProfit(self, prices):
        length_len(prices)
        __ length__0:
            r_ 0
        f1_[0 ___ i __ ra..(length)]
        f2_[0 ___ i __ ra..(length)]
        minV _ prices[0]; f1[0]_0
        ___ i __ ra..(1,length):
            minV_min(minV, prices[i])
            f1[i]_ma.(f1[i-1],prices[i]-minV)
        maxV_prices[length-1]; f2[length-1]_0
        ___ i __ ra..(length-2,-1,-1):
            maxV_ma.(maxV,prices[i])
            f2[i]_ma.(f2[i+1],maxV-prices[i])
        res_0
        ___ i __ ra..(length):
            __ f1[i]+f2[i]>res: res_f1[i]+f2[i]
        r_ res


Solution().maxProfit([1, 4, 8, 1, 2])