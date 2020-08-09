'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object
    ___ isPowerOfThree(self, n
        __ n <= 0: r_ False
        r_ (3**19)%n __ 0
    
    ___ isPowerOfThreeMath(self, n
        __ n <= 0: r_ False
        w___ n > 1:
            __ n % 3 != 0:
                r_ False
            n = n/3
        r_ True
