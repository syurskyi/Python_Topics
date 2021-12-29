"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not
ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
__author__ = 'Daniel'


class Solution(object):
    ___ isUgly(self, num):
        """
        Prime factors: 2, 3, 5

        :type num: int
        :rtype: bool
        """
        __ num < 1:
            r.. False
        __ num __ 1:
            r.. True

        ugly = {2, 3, 5}

        prime = 2
        while prime*prime <= num and num > 1:
            __ num % prime != 0:
                prime += 1
            ____:
                num /= prime
                __ prime n.. __ ugly:
                    r.. False

        __ num n.. __ ugly:
            r.. False

        r.. True