"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
__author__ = 'Daniel'


class Solution:
    ___ convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        sb    # list  # string builder
        while n:
            n -= 1  # there is not 0 representation in excel title
            sb.a..(chr(ord("A")+n%26))
            n /= 26

        r.. "".join(reversed(sb))

