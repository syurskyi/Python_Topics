c_ Solution:
    """
    @param A: An integer array
    @param K: A positive integer (K <= length(A))
    @param target: An integer
    @return: An integer
    """
    ___ kSum  A, K, target
        n l..(A)

        """
        `dp[i][j][k]` means the ways we can take `j` in previous `i` nums and its sum equals `k`
        """
        dp [[[0] * (target + 1) ___ _ __ r..(K + 1)] ___ _ __ r..(n + 1)]

        ___ i __ r..(n + 1
            dp[i][0][0] 1

        ___ i __ r..(1, n + 1
            ___ j __ r..(1, m..(K, i) + 1
                ___ k __ r..(1, target + 1
                    __ k >_ A[i - 1]:
                        dp[i][j][k] += dp[i - 1][j - 1][k - A[i - 1]]

                    dp[i][j][k] += dp[i - 1][j][k]

        r.. dp[n][K][target]
