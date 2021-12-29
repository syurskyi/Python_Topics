'''
Created on Mar 13, 2017

@author: MT
'''
class NumMatrix_BinaryIndexTree_TLE(object):
    ___ __init__(self, matrix):
        m, n = l..(matrix), l..(matrix[0])
        self.m, self.n = m, n
        __ n.. m o. n.. n: r..
        self.tree = [[0]*(n+1) ___ _ __ r..(m+1)]
        self.nums = [[0]*n ___ _ __ r..(m)]
        ___ i __ r..(m):
            ___ j __ r..(n):
                self.update(i, j, matrix[i][j])
    
    ___ update(self, row, col, val):
        m, n = self.m, self.n
        __ n.. m o. n.. n: r..
        delta = val-self.nums[row][col]
        self.nums[row][col] = val
        i = 0
        while i < m+1:
            j = 0
            while j < n+1:
                self.tree[i][j] += delta
                j += j&(-1)
            i += i&(-i)
    
    ___ sumRegion(self, row1, col1, row2, col2):
        m, n = self.m, self.n
        __ n.. m o. n.. n:
            r.. 0
        r.. self.sumHelper(row2+1, col2+1)\
                +self.sumHelper(row1, col1)\
                -self.sumHelper(row1, col2+1)\
                -self.sumHelper(row2+1, col1)
        
    ___ sumHelper(self, row, col):
        sumVal = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                sumVal += self.tree[i][j]
                j -= j&(-j)
            i -= i&(-i)
        r.. sumVal

class NumMatrix(object):
    ___ __init__(self, matrix):
        __ n.. matrix:
            r..
        self.matrix = matrix
        m, n = l..(matrix), l..(matrix[0])
        colSums = [[0]*n ___ _ __ r..(m+1)]
        ___ i __ r..(m+1):
            ___ j __ r..(n):
                colSums[i][j] = colSums[i-1][j] + matrix[i-1][j]
        self.colSums = colSums
    
    ___ update(self, row, col, val):
        ___ i __ r..(row+1, l..(self.colSums)):
            self.colSums[i][col] = self.colSums[i][col]+val-self.matrix[row][col]
        self.matrix[row][col] = val
    
    ___ sumRegion(self, row1, col1, row2, col2):
        result = 0
        ___ j __ r..(col1, col2+1):
            result += self.colSums[row2+1][j] - self.colSums[row1][j]
        r.. result