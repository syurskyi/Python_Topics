'''
Created on Jan 23, 2017

@author: MT
'''

c_ Solution(o..
    ___ minDistance  word1, word2
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = l..(word1)
        m = l..(word2)
        dp = [[0]*(m+1) ___ i __ r..(n+1)]
        ___ i __ r..(n+1
            dp[i][0] = i
        ___ j __ r..(m+1
            dp[0][j] = j
        ___ i __ r..(0, n
            c1 = word1[i]
            ___ j __ r..(0, m
                c2 = word2[j]
                __ c1 __ c2:
                    dp[i+1][j+1] = dp[i][j]
                ____:
                    r.. = dp[i][j] + 1
                    insert = dp[i][j+1] + 1
                    delete = dp[i+1][j] + 1
                    dp[i+1][j+1] = m..((r.., insert, delete
        r.. dp[-1][-1]
    
    ___ test
        testCases = [
            ('', 'a'),
            ('horse', 'rose'),
            ('horse', 'ros'),
        ]
        ___ word1, word2 __ testCases:
            print('word1: %s' % (word1
            print('word2: %s' % (word2
            result = minDistance(word1, word2)
            print('result: %s' % (result
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()