'''
Created on Jan 22, 2017

@author: MT
'''
c_ Solution(object):
    ___ isNumber(self, s):
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
            __ c.isdigit():
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
        pass

__ __name__ __ '__main__':
    Solution().test()