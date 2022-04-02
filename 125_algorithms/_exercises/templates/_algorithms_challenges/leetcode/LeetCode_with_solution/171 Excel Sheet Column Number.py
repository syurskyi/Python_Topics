"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""
__author__ = 'Daniel'


c_ Solution:
    ___ titleToNumber  s
        """
        :type s: str
        :rtype: int
        """
        sig = 1
        ret = 0
        ___ i __ x..(l..(s)-1, -1, -1
            ret += sig*(o..(s[i])-o..('A')+1)
            sig *= 26

        r.. ret