'''
Created on Apr 24, 2018

@author: tongq
'''
c_ Solution(o..
    ___ numberOfLines  widths, S
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        s = S
        res = [1, 0]
        ___ c __ s:
            __ res[1] + widths[o..(c)-o..('a')] <= 100:
                res[1] += widths[o..(c)-o..('a')]
            ____
                res[0] += 1
                res[1] = widths[o..(c)-o..('a')]
        r.. res
