'''
Created on Jan 23, 2017

@author: MT
'''

c_ Solution(object):
    ___ setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        isColEmpty, isRowEmpty = F.., F..
        ___ i __ r..(l..(matrix)):
            __ matrix[i][0] __ 0:
                isColEmpty = T..
                break
        ___ i __ r..(l..(matrix[0])):
            __ matrix[0][i] __ 0:
                isRowEmpty = T..
                break
        ___ i __ r..(1, l..(matrix)):
            ___ j __ r..(1, l..(matrix[0])):
                __ matrix[i][j] __ 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        ___ i __ r..(1, l..(matrix)):
            __ matrix[i][0] __ 0:
                ___ j __ r..(1, l..(matrix[0])):
                    matrix[i][j] = 0
        ___ j __ r..(1, l..(matrix[0])):
            __ matrix[0][j] __ 0:
                ___ i __ r..(1, l..(matrix)):
                    matrix[i][j] = 0
        __ isColEmpty:
            ___ i __ r..(l..(matrix)):
                matrix[i][0] = 0
        __ isRowEmpty:
            ___ j __ r..(l..(matrix[0])):
                matrix[0][j] = 0
    
    ___ test
        pass

Solution().test()