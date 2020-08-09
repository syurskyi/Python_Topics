"""
DP: MLE
"""
class Solution:
    """
    @param: A: an integer array and all positive numbers
    @param: target: An integer
    @return: An integer
    """
    ___ backPackV(self, A, target
        __ not A:
            r_ 0

        n = le.(A)
        dp = [[0] * (target + 1) ___ _ in range(n + 1)]
        dp[0][0] = 1

        ___ i in range(1, n + 1
            ___ j in range(target + 1
                dp[i][j] = dp[i - 1][j]
                __ j >= A[i - 1]:
                    dp[i][j] += dp[i - 1][j - A[i - 1]]

        r_ dp[n][target]


"""
DP: optimized space complexity
"""
class Solution:
    """
    @param: A: an integer array and all positive numbers
    @param: target: An integer
    @return: An integer
    """
    ___ backPackV(self, A, target
        __ not A:
            r_ 0

        n = le.(A)
        dp = [0] * (target + 1)
        dp[0] = 1

        ___ i in range(n
            ___ j in range(target, A[i] - 1, -1
                dp[j] += dp[j - A[i]]

        r_ dp[target]
