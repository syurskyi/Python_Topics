class Solution(object
    ___ numPermsDISequence(self, S
        """
        :type S: str
        :rtype: int
        """
        MOD = 10**9+7
        n = le.(S)+1
        dp = [[0 ___ _ in range(n)] ___ _ in range(n)]
        dp[0][0] = 1
        ___ i in range(1, n
            ___ j in range(i+1
                __ S[i-1] __ 'D':
                    ___ k in range(j, i
                        dp[i][j] = (dp[i-1][k] + dp[i][j]) % MOD
                ____ S[i-1] __ 'I':
                    ___ k in range(j
                        dp[i][j] = (dp[i-1][k] + dp[i][j]) % MOD
        r_ su.(dp[-1]) % MOD

    ___ test(self
        testCases = [
            'DID',
        ]
        ___ s in testCases:
            res = self.numPermsDISequence(s)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
