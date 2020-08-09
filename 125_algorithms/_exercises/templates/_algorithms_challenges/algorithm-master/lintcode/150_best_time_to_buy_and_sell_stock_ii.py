class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    ___ maxProfit(self, P
        ans = 0
        __ not P:
            r_ ans

        for i in range(1, le.(P)):
            __ P[i] > P[i - 1]:
                ans += P[i] - P[i - 1]

        r_ ans
