'''
Created on Apr 24, 2018

@author: tongq
'''
c_ Solution(object):
    ___ numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        s = S
        res = [1, 0]
        ___ c __ s:
            __ res[1] + widths[ord(c)-ord('a')] <= 100:
                res[1] += widths[ord(c)-ord('a')]
            ____:
                res[0] += 1
                res[1] = widths[ord(c)-ord('a')]
        r.. res
