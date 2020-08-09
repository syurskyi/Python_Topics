'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object
    ___ reverse(self, x
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sig = 1 __ x >= 0 else -1
        x = abs(x)
        w___ x > 0:
            digit = x%10
            res = res*10 + digit
            x = (x-digit)//10
        res = res*sig
        __ res > 2**31-1 or res < -2**31:
            r_ 0
        ____
            r_ res
