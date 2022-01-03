'''
Created on Mar 11, 2017

@author: MT
'''

c_ NumMatrix(object):
    ___ - , matrix):
        __ n.. matrix:
            tbl = N..
            r..
        m, n = l..(matrix), l..(matrix[0])
        tbl = [[0]*(n+1) ___ _ __ r..(m+1)]
        ___ i __ r..(m):
            ___ j __ r..(n):
                tbl[i+1][j+1] = tbl[i][j+1]+tbl[i+1][j]+matrix[i][j]-tbl[i][j]
        tbl = tbl
    
    ___ sumRegion(self, row1, col1, row2, col2):
        r.. tbl[row2+1][col2+1] -\
            tbl[row2+1][col1] -\
            tbl[row1][col2+1]+\
            tbl[row1][col1]

__ __name__ __ '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    numMatrix = NumMatrix(matrix)
    print(numMatrix.sumRegion(2, 1, 4, 3))
    print(numMatrix.sumRegion(1, 1, 2, 2))
    print(numMatrix.sumRegion(1, 2, 2, 4))
    print('-='*30+'-')
