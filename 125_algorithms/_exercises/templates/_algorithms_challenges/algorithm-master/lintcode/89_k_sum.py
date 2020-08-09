class Solution:
    """
    @param A: An integer array
    @param K: A positive integer (K <= length(A))
    @param target: An integer
    @return: An integer
    """
    ___ kSum(self, A, K, target
        n = le.(A)

        """
        `dp[i][j][k]` means the ways we can take `j` in previous `i` nums and its sum equals `k`
        """
        dp = [[[0] * (target + 1) ___ _ in range(K + 1)] ___ _ in range(n + 1)]

        ___ i in range(n + 1
            dp[i][0][0] = 1

        ___ i in range(1, n + 1
            ___ j in range(1, min(K, i) + 1
                ___ k in range(1, target + 1
                    __ k >= A[i - 1]:
                        dp[i][j][k] += dp[i - 1][j - 1][k - A[i - 1]]

                    dp[i][j][k] += dp[i - 1][j][k]

        r_ dp[n][K][target]
