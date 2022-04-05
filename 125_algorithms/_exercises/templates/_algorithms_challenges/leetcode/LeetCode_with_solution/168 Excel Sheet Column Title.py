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


c_ Solution:
    ___ convertToTitle  n
        """
        :type n: int
        :rtype: str
        """
        sb    # list  # string builder
        w.... n:
            n -_ 1  # there is not 0 representation in excel title
            sb.a..(chr(o..("A")+n%26
            n /= 26

        r.. "".j..(r..(sb

