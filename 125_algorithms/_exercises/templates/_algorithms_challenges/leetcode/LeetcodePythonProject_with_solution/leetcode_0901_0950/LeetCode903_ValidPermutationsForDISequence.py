c_ Solution(o..
    ___ numPermsDISequence  S
        """
        :type S: str
        :rtype: int
        """
        MOD 10**9+7
        n l..(S)+1
        dp [[0 ___ _ __ r..(n)] ___ _ __ r..(n)]
        dp 0 0  1
        ___ i __ r..(1, n
            ___ j __ r..(i+1
                __ S[i-1] __ 'D':
                    ___ k __ r..(j, i
                        dp[i][j] (dp[i-1][k] + dp[i][j]) % MOD
                ____ S[i-1] __ 'I':
                    ___ k __ r..(j
                        dp[i][j] (dp[i-1][k] + dp[i][j]) % MOD
        r.. s..(dp[-1]) % MOD

    ___ test
        testCases [
            'DID',
        ]
        ___ s __ testCases:
            res numPermsDISequence(s)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
