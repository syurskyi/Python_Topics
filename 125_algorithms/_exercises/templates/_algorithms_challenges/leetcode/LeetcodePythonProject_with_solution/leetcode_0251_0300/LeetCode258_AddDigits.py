'''
Created on May 13, 2018

@author: tongq
'''
c_ Solution(object):
    ___ addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        r.. num-9*((num-1)/9) __ num != 0 ____ 0
    
    ___ addDigits_slow(self, num):
        w.... num >= 10:
            newNum = 0
            w.... num > 0:
                digit = num%10
                num = num//10
                newNum += digit
            num = newNum
        r.. num
