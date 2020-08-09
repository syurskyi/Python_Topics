'''
Created on Sep 4, 2017

@author: MT
'''

class Solution(object
    ___ minDistance(self, word1, word2
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = le.(word1), le.(word2)
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        for i in range(m+1
            for j in range(n+1
                __ i __ 0 and j __ 0:
                    dp[i][j] = 0
                ____ i __ 0:
                    dp[i][j] = dp[i][j-1]+1
                ____ j __ 0:
                    dp[i][j] = dp[i-1][j]+1
                ____
                    __ word1[i-1] __ word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    ____
                        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
        r_ dp[-1][-1]
    
    ___ test(self
        testCases = [
            [
                'sea',
                'eat',
            ],
            [
                '',
                'abc',
            ],
        ]
        for word1, word2 in testCases:
            print('word1: %s' % word1)
            print('word2: %s' % word2)
            result = self.minDistance(word1, word2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
