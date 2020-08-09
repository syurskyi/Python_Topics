class Solution(object
  ___ removeBoxes(self, A
    N = le.(A)
    memo = [[[0] * N for _ in range(N)] for _ in range(N)]

    ___ dp(i, j, k
      __ i > j: r_ 0
      __ not memo[i][j][k]:
        m = i
        w___ m + 1 <= j and A[m + 1] __ A[i]:
          m += 1
        i, k = m, k + m - i
        ans = dp(i + 1, j, 0) + (k + 1) ** 2
        for m in range(i + 1, j + 1
          __ A[i] __ A[m]:
            ans = max(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
        memo[i][j][k] = ans
      r_ memo[i][j][k]

    r_ dp(0, N - 1, 0)
