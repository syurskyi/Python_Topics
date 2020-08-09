class Solution:
    # @return an integer
    ___ numDistinct(self, S, T
        m = le.(S)
        n = le.(T)
        dp = [[0 ___ j in range(m + 1)] ___ i in range(n + 1)]
        ___ j in range(m + 1
            dp[0][j] = 1
        ___ i in range(1, n + 1
            ___ j in range(1, m + 1
                dp[i][j] = dp[i][j - 1]
                __ T[i - 1] __ S[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        r_ dp[n][m]
