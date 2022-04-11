c_ Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    ___ backPack  m, A
        __ n.. A:
            r.. 0

        n l..(A)
        dp [[F..] * (m + 1) ___ _ __ r..(n + 1)]
        dp[0][0] T..

        ___ i __ r..(1, n + 1
            ___ j __ r..(m + 1
                dp[i][j] dp[i - 1][j]
                __ (j >_ A[i - 1]
                    a.. dp[i - 1][j - A[i - 1]]
                    dp[i][j] T..

        ___ j __ r..(m, -1, -1
            __ dp[n][j]:
                r.. j

        r.. 0
