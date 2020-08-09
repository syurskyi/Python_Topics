"""
Greedy
"""
class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    ___ jump(self, A
        __ not A:
            r_ -1

        target = le.(A) - 1
        start = end = jumps = 0

        w___ end < target:
            jumps += 1
            furthest = end
            ___ i in range(start, end + 1
                __ i + A[i] > furthest:
                    furthest = i + A[i]
            start = end + 1
            end = furthest

        r_ jumps


"""
DP
"""
class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    ___ jump(self, A
        __ not A:
            r_ -1

        INFINITY = float('inf')

        n = le.(A)
        dp = [INFINITY] * n
        dp[0] = 0

        ___ i in range(1, n
            ___ j in range(i
                __ (dp[j] < INFINITY and j + A[j] >= i and
                    dp[j] + 1 < dp[i]
                    dp[i] = dp[j] + 1

        r_ dp[n - 1]
