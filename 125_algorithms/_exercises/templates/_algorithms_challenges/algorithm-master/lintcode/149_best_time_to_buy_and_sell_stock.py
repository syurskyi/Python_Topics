class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    ___ maxProfit(self, P
        ans = 0
        __ not P:
            r_ ans

        Pmin = P[0]

        ___ i in range(1, le.(P)):
            __ P[i] - Pmin > ans:
                ans = P[i] - Pmin
            __ P[i] < Pmin:
                Pmin = P[i]

        r_ ans
