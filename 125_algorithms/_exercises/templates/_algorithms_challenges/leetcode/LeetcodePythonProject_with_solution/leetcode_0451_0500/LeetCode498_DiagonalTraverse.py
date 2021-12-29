'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ findDiagonalOrder(self, matrix):
        __ not matrix or not matrix[0]: return []
        __ len(matrix) == 1: return matrix[0]
        __ len(matrix[0]) == 1: return [row[0] for row in matrix]
        rev = False
        result = []
        m, n = len(matrix), len(matrix[0])
        for l in range(m+n-1):
            __ rev:
                for i in range(l+1):
                    j = l-i
                    __ 0 <= i < m and 0 <= j < n:
                        result.append(matrix[i][j])
            else:
                for j in range(l+1):
                    i = l-j
                    __ 0 <= i < m and 0 <= j < n:
                        result.append(matrix[i][j])
            rev = not rev
        return result
