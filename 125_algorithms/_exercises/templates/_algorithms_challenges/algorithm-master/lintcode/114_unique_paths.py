class Solution:
    ___ uniquePaths(self, m, n
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n ___ _ in range(m)]

        ___ x in range(1, m
            ___ y in range(1, n
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

        r_ dp[m - 1][n - 1]
