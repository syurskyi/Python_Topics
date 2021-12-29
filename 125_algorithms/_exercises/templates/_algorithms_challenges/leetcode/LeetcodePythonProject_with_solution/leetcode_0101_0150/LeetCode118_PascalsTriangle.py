'''
Created on May 29, 2018

@author: tongq
'''
class Solution(object):
    ___ generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        __ numRows <= 0: return []
        res = [[1]]
        for i in range(1, numRows):
            tmp = []
            for j in range(i+1):
                __ j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(res[i-1][j] + res[i-1][j-1])
            res.append(tmp)
        return res
