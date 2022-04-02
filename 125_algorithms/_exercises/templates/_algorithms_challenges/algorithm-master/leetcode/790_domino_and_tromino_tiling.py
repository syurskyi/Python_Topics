c_ Solution:
    ___ numTilings  N
        """
        :type N: int
        :rtype: int
        """
        __ N < 3:
            r.. N

        MOD = 10 ** 9 + 7
        dp = [0] * (N + 1)
        dp[:3] = 1, 1, 2

        ___ i __ r..(3, N + 1
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % MOD

        r.. dp[N]
