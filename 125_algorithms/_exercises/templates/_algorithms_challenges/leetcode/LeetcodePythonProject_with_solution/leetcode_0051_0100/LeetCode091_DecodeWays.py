'''
Created on Jan 28, 2017

@author: MT
'''

c_ Solution(o..
    ___ numDecodings  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s: r.. 0
        n = l..(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 0 __ s[0] __ '0' ____ 1
        ___ i __ r..(2, n+1
            first = i..(s[i-1])
            second = i..(s[i-2:i])
            __ 1 <= first <= 9:
                dp[i] += dp[i-1]
            __ 10 <= second <= 26:
                dp[i] += dp[i-2]
        r.. dp[-1]
    
    ___ numDecodings_orig  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s o. s[0] __ '0':
            r.. 0
        __ l..(s) __ 1:
            r.. 1
        dp = [0]*(l..(s
        dp[0] = 1
        __ i..(s[0:2]) > 26:
            __ s[1] != '0':
                dp[1] = 1
            ____:
                dp[1] = 0
        ____:
            __ s[1] != '0':
                dp[1] = 2
            ____:
                dp[1] = 1
        n = l..(s)
        
        ___ i __ r..(2, n
            __ s[i] != '0':
                dp[i] += dp[i-1]
            val = i..(s[i-1:i+1])
            __ val<=26 a.. val>=10:
                dp[i] += dp[i-2]
        
        r.. dp[-1]
    
    ___ test
        testCases = [
            '111',
        ]
        ___ s __ testCases:
            print('s: %s' % (s
            result = numDecodings(s)
            print('result: %s' % (result
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()