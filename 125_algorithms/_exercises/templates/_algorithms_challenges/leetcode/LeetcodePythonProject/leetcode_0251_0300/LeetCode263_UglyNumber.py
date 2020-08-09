'''
Created on Mar 2, 2017

@author: MT
'''

class Solution(object
    ___ isUgly_noRec(self, num
        """
        :type num: int
        :rtype: bool
        """
        __ num __ 0: r_ False
        w___ num > 1:
            __ num%2 __ 0:
                num //= 2
            ____ num%3 __ 0:
                num //= 3
            ____ num%5 __ 0:
                num //= 5
            ____
                break
        r_ num __ 1
    
    ___ isUgly(self, num
        """
        :type num: int
        :rtype: bool
        """
        __ num __ 0: r_ False
        __ num __ 1: r_ True
        __ num%2 __ 0: r_ self.isUgly(num/2)
        __ num%3 __ 0: r_ self.isUgly(num/3)
        __ num%5 __ 0: r_ self.isUgly(num/5)
        r_ False
