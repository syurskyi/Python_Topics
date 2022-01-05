'''
Created on Sep 5, 2017

@author: MT
'''

c_ Solution(o..):
    ___ findIntegers  num):
        """
        :type num: int
        :rtype: int
        """
        s = '{0:b}'.f..(num)[::-1]
        n = l..(s)
        dp1 = [0]*n
        dp2 = [0]*n
        dp1[0], dp2[0] = 1, 1
        ___ i __ r..(1, n):
            dp1[i] = dp1[i-1]+dp2[i-1]
            dp2[i] = dp1[i-1]
        res = dp1[-1]+dp2[-1]
        ___ i __ r..(n-2, -1, -1):
            __ s[i] __ '1' a.. s[i+1] __ '1':
                _____
            __ s[i] __ '0' a.. s[i+1] __ '0':
                res -= dp2[i]
        r.. res
    
    ___ test
        testCases = [
            5,
            6,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = findIntegers(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
