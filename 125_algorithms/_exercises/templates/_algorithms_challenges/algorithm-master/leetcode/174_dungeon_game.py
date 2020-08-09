class Solution:
    ___ calculateMinimumHP(self, G
        """
        :type G: List[List[int]]
        :rtype: int
        """
        INFINITY = float('inf')
        m, n = le.(G), le.(G[0])
        dp = [[INFINITY] * (n + 1) ___ _ in range(m + 1)]
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        ___ i in range(m - 1, -1, -1
            ___ j in range(n - 1, -1, -1
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - G[i][j]
                __ dp[i][j] <= 0:
                    dp[i][j] = 1

        r_ dp[0][0]
