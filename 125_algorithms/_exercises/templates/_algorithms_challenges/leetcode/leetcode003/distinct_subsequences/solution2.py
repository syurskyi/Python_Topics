c_ Solution:
    # @return an integer
    ___ numDistinct(self, S, T):
        m = l..(S)
        n = l..(T)
        dp = [[0 ___ j __ r..(m + 1)] ___ i __ r..(n + 1)]
        ___ j __ r..(m + 1):
            dp[0][j] = 1
        ___ i __ r..(1, n + 1):
            ___ j __ r..(1, m + 1):
                dp[i][j] = dp[i][j - 1]
                __ T[i - 1] __ S[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        r.. dp[n][m]
