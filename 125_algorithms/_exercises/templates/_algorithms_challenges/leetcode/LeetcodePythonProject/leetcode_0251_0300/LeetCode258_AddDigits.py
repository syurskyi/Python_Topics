'''
Created on May 13, 2018

@author: tongq
'''
class Solution(object
    ___ addDigits(self, num
        """
        :type num: int
        :rtype: int
        """
        r_ num-9*((num-1)/9) __ num != 0 else 0
    
    ___ addDigits_slow(self, num
        w___ num >= 10:
            newNum = 0
            w___ num > 0:
                digit = num%10
                num = num//10
                newNum += digit
            num = newNum
        r_ num
