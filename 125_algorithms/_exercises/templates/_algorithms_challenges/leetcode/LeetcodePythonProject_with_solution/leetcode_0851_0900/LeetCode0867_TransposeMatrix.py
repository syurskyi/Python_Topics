'''
Created on Sep 30, 2019

@author: tongq
'''
c_ Solution(object):
    ___ transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        matrix = A
        m, n = l..(matrix), l..(matrix[0])
        res = [[0]*m ___ _ __ r..(n)]
        ___ i __ r..(m):
            ___ j __ r..(n):
                res[j][i] = matrix[i][j]
        r.. res
