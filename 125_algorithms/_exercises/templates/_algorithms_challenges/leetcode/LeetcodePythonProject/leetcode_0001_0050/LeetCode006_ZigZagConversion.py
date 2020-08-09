'''
Created on Jun 7, 2018

@author: tongq
'''
class Solution(object
    ___ convert(self, s, numRows
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        __ not s or le.(s) <= 1 or numRows __ 1:
            r_ s
        step = 2*numRows-2
        res = ''
        ___ i in range(numRows
            ___ j in range(i, le.(s), step
                res += s[j]
                __ i != 0 and i != numRows-1 and j+step-2*i < le.(s
                    res += s[j+step-2*i]
        r_ res
