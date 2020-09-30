'''
Created on May 10, 2017

@author: MT
'''

class Solution(object
    ___ findDiagonalOrder(self, matrix
        __ not matrix or not matrix[0]: r_   # list
        __ le.(matrix) __ 1: r_ matrix[0]
        __ le.(matrix[0]) __ 1: r_ [row[0] ___ row __ matrix]
        rev = False
        result =   # list
        m, n = le.(matrix), le.(matrix[0])
        ___ l __ range(m+n-1
            __ rev:
                ___ i __ range(l+1
                    j = l-i
                    __ 0 <= i < m and 0 <= j < n:
                        result.append(matrix[i][j])
            ____
                ___ j __ range(l+1
                    i = l-j
                    __ 0 <= i < m and 0 <= j < n:
                        result.append(matrix[i][j])
            rev = not rev
        r_ result
