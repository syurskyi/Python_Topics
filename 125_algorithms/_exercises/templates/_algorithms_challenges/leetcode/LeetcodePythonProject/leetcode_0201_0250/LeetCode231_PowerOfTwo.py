'''
Created on Feb 23, 2017

@author: MT
'''

class Solution(object
    ___ isPowerOfTwo(self, n
        """
        :type n: int
        :rtype: bool
        """
        __ n <= 0: r_ False
        r_ bool(n&(n-1)__0)
    
    ___ isPowerOfTwoSlow(self, n
        """
        :type n: int
        :rtype: bool
        """
        __ n __ 0: r_ False
        __ n __ 1: r_ True
        __ n % 2 != 0:
            r_ False
        r_ self.isPowerOfTwo(n/2)