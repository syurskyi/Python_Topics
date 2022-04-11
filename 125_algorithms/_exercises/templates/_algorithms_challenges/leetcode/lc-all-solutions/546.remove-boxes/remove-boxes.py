c_ Solution(o..
  ___ removeBoxes  A
    N l..(A)
    memo [[[0] * N ___ _ __ r..(N)] ___ _ __ r..(N)]

    ___ dp(i, j, k
      __ i > j: r.. 0
      __ n.. memo[i][j][k]:
        m i
        w.... m + 1 <_ j a.. A[m + 1] __ A[i]:
          m += 1
        i, k m, k + m - i
        ans dp(i + 1, j, 0) + (k + 1) ** 2
        ___ m __ r..(i + 1, j + 1
          __ A[i] __ A[m]:
            ans m..(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1
        memo[i][j][k] ans
      r.. memo[i][j][k]

    r.. dp(0, N - 1, 0)
