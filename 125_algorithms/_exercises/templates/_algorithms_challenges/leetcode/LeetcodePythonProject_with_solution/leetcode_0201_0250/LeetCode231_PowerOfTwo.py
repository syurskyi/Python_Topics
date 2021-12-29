'''
Created on Feb 23, 2017

@author: MT
'''

class Solution(object):
    ___ isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        __ n <= 0: return False
        return bool(n&(n-1)==0)
    
    ___ isPowerOfTwoSlow(self, n):
        """
        :type n: int
        :rtype: bool
        """
        __ n == 0: return False
        __ n == 1: return True
        __ n % 2 != 0:
            return False
        return self.isPowerOfTwo(n/2)