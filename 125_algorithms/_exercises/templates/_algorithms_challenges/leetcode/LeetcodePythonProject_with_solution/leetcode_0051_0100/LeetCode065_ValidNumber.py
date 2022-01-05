'''
Created on Jan 22, 2017

@author: MT
'''
c_ Solution(o..):
    ___ isNumber  s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.s..
        s = s.lstrip('-')
        s = s.lstrip('+')
        i = 0
        num, dot, exp = F.., F.., F..
        w.... i < l..(s):
            c = s[i]
            __ c.i..
                num = T..
            ____ c __ '.':
                __ exp o. dot:
                    r.. F..
                dot = T..
            ____ c __ 'e':
                __ exp o. n.. num:
                    r.. F..
                exp = T..
                num = F..
            ____ c __ '+' o. c __ '-':
                __ s[i-1] != 'e':
                    r.. F..
            ____:
                r.. F..
            i += 1
        r.. num
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()