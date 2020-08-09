'''
Created on May 29, 2018

@author: tongq
'''
class Solution(object
    ___ generate(self, numRows
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        __ numRows <= 0: r_ []
        res = [[1]]
        ___ i in range(1, numRows
            tmp = []
            ___ j in range(i+1
                __ j __ 0 or j __ i:
                    tmp.append(1)
                ____
                    tmp.append(res[i-1][j] + res[i-1][j-1])
            res.append(tmp)
        r_ res
