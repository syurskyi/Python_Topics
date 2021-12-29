"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
__author__ = 'Daniel'


class Solution:
    ___ addDigits(self, num):
        """
        Enumerate and find the pattern

        Prove pattern:
        num = a0 * 10^0 + a1*10^1 + a2*10^2 ...
        addDigits(num) = a0 + a1 + a2 ... = num%9

        Formal name: digital root

        :type num:
        :rtype: int
        """
        digit = num % 9
        __ digit __ 0 and num != 0:
            r.. 9
        ____:
            r.. digit