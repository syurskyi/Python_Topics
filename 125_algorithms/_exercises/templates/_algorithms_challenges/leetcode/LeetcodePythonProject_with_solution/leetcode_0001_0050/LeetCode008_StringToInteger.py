'''
Created on Nov 8, 2017

@author: MT
'''
c_ Solution(o..
    ___ myAtoi  s..
        """
        :type str: str
        :rtype: int
        """
        s s..
        s s.s..
        __ n.. s o. s __ '+': r.. 0
        sig 1
        __ s[0] __ '+':
            s s[1:]
        ____ s[0] __ '-':
            s s[1:]
            sig -1
        s s.l..('0')
        res 0
        ___ c __ s:
            __ n.. c.i..
                _____
            res 10*res + o..(c) - o..('0')
        __ sig > 0:
            r.. m..(2**32-1, res)
        ____
            r.. m..(-2**31, sig*res)
    
    ___ test
        testCases [
            '    010',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result myAtoi(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
