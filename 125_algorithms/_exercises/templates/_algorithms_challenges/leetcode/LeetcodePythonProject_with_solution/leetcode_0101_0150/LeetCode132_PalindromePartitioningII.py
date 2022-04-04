'''
Created on Feb 8, 2017

@author: MT
'''

c_ Solution(o..
    ___ minCut  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s: r.. 0
        n = l..(s)
        dp = [[F..]*n ___ _ __ r..(n)]
        cuts = l..(r..(n
        ___ i __ r..(n
            ___ j __ r..(i, -1, -1
                __ s[i] __ s[j] a.. (i-j<=1 o. dp[j+1][i-1]
                    dp[j][i] = T..
                    __ j > 0:
                        cuts[i] = m..(cuts[i], cuts[j-1]+1)
                    ____:
                        cuts[i] = 0
        r.. cuts[-1]
    
    ___ test
        testCases = [
            'abba',
            'aab',
            'aca'
        ]
        ___ s __ testCases:
            print('s: %s' % (s
            result = minCut(s)
            print('result: %s' % (result
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
