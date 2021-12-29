'''
Created on May 29, 2018

@author: tongq
'''
class Solution(object):
    ___ getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        ___ i __ r..(rowIndex):
            newRes    # list
            ___ j __ r..(i+2):
                __ j __ 0 o. j __ i+1:
                    newRes.a..(1)
                ____:
                    newRes.a..(res[j-1]+res[j])
            res = newRes
        r.. res
