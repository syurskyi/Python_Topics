class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    ___ maxProfit(self, P):
        ans = 0
        __ not P:
            return ans

        for i in range(1, len(P)):
            __ P[i] > P[i - 1]:
                ans += P[i] - P[i - 1]

        return ans
