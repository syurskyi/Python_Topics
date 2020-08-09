'''
Created on May 29, 2018

@author: tongq
'''
class Solution(object
    ___ getRow(self, rowIndex
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        ___ i in range(rowIndex
            newRes = []
            ___ j in range(i+2
                __ j __ 0 or j __ i+1:
                    newRes.append(1)
                ____
                    newRes.append(res[j-1]+res[j])
            res = newRes
        r_ res
