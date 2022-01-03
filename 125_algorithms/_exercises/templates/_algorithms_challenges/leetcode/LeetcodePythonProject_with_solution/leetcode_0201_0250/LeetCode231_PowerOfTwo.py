'''
Created on Feb 23, 2017

@author: MT
'''

c_ Solution(object):
    ___ isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        __ n <= 0: r.. F..
        r.. bool(n&(n-1)__0)
    
    ___ isPowerOfTwoSlow(self, n):
        """
        :type n: int
        :rtype: bool
        """
        __ n __ 0: r.. F..
        __ n __ 1: r.. T..
        __ n % 2 != 0:
            r.. F..
        r.. isPowerOfTwo(n/2)