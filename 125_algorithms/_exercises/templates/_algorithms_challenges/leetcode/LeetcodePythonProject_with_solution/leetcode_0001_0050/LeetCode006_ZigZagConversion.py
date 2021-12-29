'''
Created on Jun 7, 2018

@author: tongq
'''
class Solution(object):
    ___ convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        __ n.. s o. l..(s) <= 1 o. numRows __ 1:
            r.. s
        step = 2*numRows-2
        res = ''
        ___ i __ r..(numRows):
            ___ j __ r..(i, l..(s), step):
                res += s[j]
                __ i != 0 and i != numRows-1 and j+step-2*i < l..(s):
                    res += s[j+step-2*i]
        r.. res
