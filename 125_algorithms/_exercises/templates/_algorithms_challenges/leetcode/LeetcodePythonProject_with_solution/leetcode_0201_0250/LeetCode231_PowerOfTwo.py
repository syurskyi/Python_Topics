'''
Created on Feb 23, 2017

@author: MT
'''

c_ Solution(o..
    ___ isPowerOfTwo  n
        """
        :type n: int
        :rtype: bool
        """
        __ n <_ 0: r.. F..
        r.. b..(n&(n-1)__0)
    
    ___ isPowerOfTwoSlow  n
        """
        :type n: int
        :rtype: bool
        """
        __ n __ 0: r.. F..
        __ n __ 1: r.. T..
        __ n % 2 != 0:
            r.. F..
        r.. isPowerOfTwo(n/2)