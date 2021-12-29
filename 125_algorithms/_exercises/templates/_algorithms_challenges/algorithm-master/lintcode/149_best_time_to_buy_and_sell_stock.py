class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    ___ maxProfit(self, P):
        ans = 0
        __ not P:
            return ans

        Pmin = P[0]

        for i in range(1, len(P)):
            __ P[i] - Pmin > ans:
                ans = P[i] - Pmin
            __ P[i] < Pmin:
                Pmin = P[i]

        return ans
