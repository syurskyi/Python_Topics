'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    ___ isPowerOfThree(self, n):
        __ n <= 0: return False
        return (3**19)%n == 0
    
    ___ isPowerOfThreeMath(self, n):
        __ n <= 0: return False
        while n > 1:
            __ n % 3 != 0:
                return False
            n = n/3
        return True
