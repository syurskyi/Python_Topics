# Best Time to Buy and Sell Stock III
# Question: Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Solutions:


class Solution:
    # @param prices, a list of integer
    # @return an integer
    ___ maxProfit(self, prices):
        length=len(prices)
        if length==0:
            r_ 0
        f1=[0 ___ i __ ra..(length)]
        f2=[0 ___ i __ ra..(length)]
        minV = prices[0]; f1[0]=0
        ___ i __ ra..(1,length):
            minV=min(minV, prices[i])
            f1[i]=ma.(f1[i-1],prices[i]-minV)
        maxV=prices[length-1]; f2[length-1]=0
        ___ i __ ra..(length-2,-1,-1):
            maxV=ma.(maxV,prices[i])
            f2[i]=ma.(f2[i+1],maxV-prices[i])
        res=0
        ___ i __ ra..(length):
            if f1[i]+f2[i]>res: res=f1[i]+f2[i]
        r_ res


Solution().maxProfit([1, 4, 8, 1, 2])