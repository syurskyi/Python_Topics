class Solution(object):
    ___ numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        MOD = 10**9+7
        n = len(S)+1
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            for j in range(i+1):
                __ S[i-1] == 'D':
                    for k in range(j, i):
                        dp[i][j] = (dp[i-1][k] + dp[i][j]) % MOD
                elif S[i-1] == 'I':
                    for k in range(j):
                        dp[i][j] = (dp[i-1][k] + dp[i][j]) % MOD
        return sum(dp[-1]) % MOD

    ___ test(self):
        testCases = [
            'DID',
        ]
        for s in testCases:
            res = self.numPermsDISequence(s)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
