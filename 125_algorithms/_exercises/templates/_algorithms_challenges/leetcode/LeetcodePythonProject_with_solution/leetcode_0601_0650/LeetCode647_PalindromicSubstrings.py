'''
Created on Oct 1, 2017

@author: MT
'''
c_ Solution(o..):
    ___ countSubstrings  s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s: r.. 0
        n = l..(s)
        dp = [[F..]*n ___ _ __ r..(n)]
        res = 0
        ___ i __ r..(n):
            ___ j __ r..(i, -1, -1):
                __ s[i] __ s[j] a.. (i-j<=1 o. dp[i-1][j+1]):
                    dp[i][j] = T..
                    res += 1
        r.. res
    
    ___ test
        testCases = [
            'abc',
            'aaa',
            'aaaaa',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = countSubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
