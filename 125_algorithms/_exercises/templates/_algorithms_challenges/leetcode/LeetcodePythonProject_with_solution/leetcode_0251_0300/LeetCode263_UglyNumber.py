'''
Created on Mar 2, 2017

@author: MT
'''

c_ Solution(o..
    ___ isUgly_noRec  num
        """
        :type num: int
        :rtype: bool
        """
        __ num __ 0: r.. F..
        w.... num > 1:
            __ num%2 __ 0:
                num //= 2
            ____ num%3 __ 0:
                num //= 3
            ____ num%5 __ 0:
                num //= 5
            ____
                _____
        r.. num __ 1
    
    ___ isUgly  num
        """
        :type num: int
        :rtype: bool
        """
        __ num __ 0: r.. F..
        __ num __ 1: r.. T..
        __ num%2 __ 0: r.. isUgly(num/2)
        __ num%3 __ 0: r.. isUgly(num/3)
        __ num%5 __ 0: r.. isUgly(num/5)
        r.. F..
