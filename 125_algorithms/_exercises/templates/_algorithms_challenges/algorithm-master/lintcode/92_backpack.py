class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    ___ backPack(self, m, A
        __ not A:
            r_ 0

        n = le.(A)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1
            for j in range(m + 1
                dp[i][j] = dp[i - 1][j]
                __ (j >= A[i - 1]
                    and dp[i - 1][j - A[i - 1]]
                    dp[i][j] = True

        for j in range(m, -1, -1
            __ dp[n][j]:
                r_ j

        r_ 0
