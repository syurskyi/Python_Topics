'''
Created on Feb 23, 2017

@author: MT
'''
c_ Solution(o..
    ___ countDigitOne  n
        """
        :type n: int
        :rtype: int
        """
        __ n <_ 0: r.. 0
        q, x, res n, 1, 0
        w.... q > 0:
            digit q%10
            q //= 10
            res += q*x
            __ digit __ 1:
                res += n%x+1
            ____ digit > 1:
                res += x
            x *= 10
        r.. res
