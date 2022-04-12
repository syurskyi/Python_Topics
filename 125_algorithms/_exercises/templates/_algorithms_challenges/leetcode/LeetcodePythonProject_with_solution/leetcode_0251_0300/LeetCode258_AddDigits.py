'''
Created on May 13, 2018

@author: tongq
'''
c_ Solution(o..
    ___ addDigits  num
        """
        :type num: int
        :rtype: int
        """
        r.. num-9*((num-1)/9) __ num !_ 0 ____ 0
    
    ___ addDigits_slow  num
        w.... num >_ 10:
            newNum 0
            w.... num > 0:
                digit num%10
                num num//10
                newNum += digit
            num newNum
        r.. num
