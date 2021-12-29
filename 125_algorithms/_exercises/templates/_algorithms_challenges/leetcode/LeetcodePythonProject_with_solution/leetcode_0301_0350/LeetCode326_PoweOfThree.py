'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    ___ isPowerOfThree(self, n):
        __ n <= 0: r.. False
        r.. (3**19)%n __ 0
    
    ___ isPowerOfThreeMath(self, n):
        __ n <= 0: r.. False
        w.... n > 1:
            __ n % 3 != 0:
                r.. False
            n = n/3
        r.. True
