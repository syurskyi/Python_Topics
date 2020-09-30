'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object
    ___ transpose(self, A
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        matrix = A
        m, n = le.(matrix), le.(matrix[0])
        res = [[0]*m ___ _ __ range(n)]
        ___ i __ range(m
            ___ j __ range(n
                res[j][i] = matrix[i][j]
        r_ res
