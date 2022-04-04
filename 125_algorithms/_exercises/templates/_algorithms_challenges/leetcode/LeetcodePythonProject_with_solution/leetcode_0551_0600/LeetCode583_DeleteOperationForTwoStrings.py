'''
Created on Sep 4, 2017

@author: MT
'''

c_ Solution(o..
    ___ minDistance  word1, word2
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = l..(word1), l..(word2)
        dp = [[f__('inf')]*(n+1) ___ _ __ r..(m+1)]
        ___ i __ r..(m+1
            ___ j __ r..(n+1
                __ i __ 0 a.. j __ 0:
                    dp[i][j] = 0
                ____ i __ 0:
                    dp[i][j] = dp[i][j-1]+1
                ____ j __ 0:
                    dp[i][j] = dp[i-1][j]+1
                ____
                    __ word1[i-1] __ word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    ____
                        dp[i][j] = m..(dp[i-1][j]+1, dp[i][j-1]+1)
        r.. dp[-1][-1]
    
    ___ test
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
        ___ word1, word2 __ testCases:
            print('word1: %s' % word1)
            print('word2: %s' % word2)
            result = minDistance(word1, word2)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
