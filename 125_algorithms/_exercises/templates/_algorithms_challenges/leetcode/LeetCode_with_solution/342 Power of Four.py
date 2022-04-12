"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


__author__ 'Daniel'


c_ Solution(o..
    ___ isPowerOfFour  num
        """
        Modular calculation
        4^a mod 3
         = (1)^a mod 3
         = 1
        :param num:
        :return:
        """
        __ num < 1:
            r.. F..
        __ num & num -1 !_ 0:
            r.. F..

        r.. num % 3 __ 1

    ___ isPowerOfFourNaive  num
        """
        Naive Determine number of 0 bits to be even
        :type num: int
        :rtype: bool
        """
        __ num < 1:
            r.. F..
        __ num & num-1 !_ 0:
            r.. F..

        w... T...
            __ num __ 0:
                r.. F..
            ____ num __ 1:
                r.. T..

            num >>= 2