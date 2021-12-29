class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    ___ maxProfit(self, P):
        ans = 0
        __ n.. P:
            r.. ans

        Pmin = P[0]

        ___ i __ r..(1, l..(P)):
            __ P[i] - Pmin > ans:
                ans = P[i] - Pmin
            __ P[i] < Pmin:
                Pmin = P[i]

        r.. ans
