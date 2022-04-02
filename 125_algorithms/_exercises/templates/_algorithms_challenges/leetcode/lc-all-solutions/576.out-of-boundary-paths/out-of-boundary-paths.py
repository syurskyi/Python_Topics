c_ Solution(o..
  ___ findPaths  m, n, N, x, y
    dp = [[[0] * n ___ _ __ r..(m)] ___ _ __ r..(N + 1)]
    dp[0][x][y] = 1
    ans = 0
    mod = 10 ** 9 + 7
    ___ k __ r..(1, N + 1
      ___ i __ r..(m
        ___ j __ r..(n
          __ i __ 0:
            ans += dp[k - 1][i][j] % mod
          __ i __ m - 1:
            ans += dp[k - 1][i][j] % mod
          __ j __ 0:
            ans += dp[k - 1][i][j] % mod
          __ j __ n - 1:
            ans += dp[k - 1][i][j] % mod
          __ i > 0:
            dp[k][i][j] += dp[k - 1][i - 1][j]
          __ i < m - 1:
            dp[k][i][j] += dp[k - 1][i + 1][j]
          __ j > 0:
            dp[k][i][j] += dp[k - 1][i][j - 1]
          __ j < n - 1:
            dp[k][i][j] += dp[k - 1][i][j + 1]
    r.. ans % mod
