'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object
    ___ setZeroes(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        isColEmpty, isRowEmpty = False, False
        ___ i __ range(le.(matrix)):
            __ matrix[i][0] __ 0:
                isColEmpty = True
                break
        ___ i __ range(le.(matrix[0])):
            __ matrix[0][i] __ 0:
                isRowEmpty = True
                break
        ___ i __ range(1, le.(matrix)):
            ___ j __ range(1, le.(matrix[0])):
                __ matrix[i][j] __ 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        ___ i __ range(1, le.(matrix)):
            __ matrix[i][0] __ 0:
                ___ j __ range(1, le.(matrix[0])):
                    matrix[i][j] = 0
        ___ j __ range(1, le.(matrix[0])):
            __ matrix[0][j] __ 0:
                ___ i __ range(1, le.(matrix)):
                    matrix[i][j] = 0
        __ isColEmpty:
            ___ i __ range(le.(matrix)):
                matrix[i][0] = 0
        __ isRowEmpty:
            ___ j __ range(le.(matrix[0])):
                matrix[0][j] = 0
    
    ___ test(self
        pass

Solution().test()