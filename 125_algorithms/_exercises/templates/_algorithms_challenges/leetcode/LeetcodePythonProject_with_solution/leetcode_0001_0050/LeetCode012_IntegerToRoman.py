'''
Created on Nov 7, 2017

@author: MT
'''
c_ Solution(o..
    ___ intToRoman  num
        """
        :type num: int
        :rtype: str
        """
        res  ''
        nums   [1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1]
        chars   'M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
        ___ c, n __ z..(chars, nums
            times  num//n
            __ times:
                res + c*times
                num - n*times
        r.. res
