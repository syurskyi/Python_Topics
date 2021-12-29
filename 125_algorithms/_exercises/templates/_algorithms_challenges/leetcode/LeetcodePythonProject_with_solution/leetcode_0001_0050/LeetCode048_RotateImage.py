'''
Created on Jun 5, 2018

@author: tongq
'''
class Solution(object):
    ___ rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        _______ math
        n = l..(matrix)
        ___ i __ r..(n//2):
            ___ j __ r..(int(math.ceil(n/2.0))):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
