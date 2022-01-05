c_ Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    ___ maxProfit  P):
        ans = 0
        __ n.. P:
            r.. ans

        ___ i __ r..(1, l..(P)):
            __ P[i] > P[i - 1]:
                ans += P[i] - P[i - 1]

        r.. ans
