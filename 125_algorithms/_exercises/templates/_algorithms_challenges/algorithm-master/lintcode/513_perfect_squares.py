"""
Test Case:

1
"""


c_ Solution:
    """
    @param: n: a positive integer
    @return: An integer
    """
    ___ numSquares  n):
        __ n <= 0:
            r.. 0

        INFINITY = f__('inf')

        # `dp[i]` means the least number of perfect square numbers of `i`
        dp = [INFINITY] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        ___ i __ r..(1, n + 1):
            j = 1
            w.... j * j <= i:
                dp[i] = m..(dp[i], dp[i - j * j] + 1)
                j += 1

        r.. dp[n]
