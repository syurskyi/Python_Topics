'''
Created on Mar 13, 2017

@author: MT
'''
class NumMatrix_BinaryIndexTree_TLE(object
    ___ __init__(self, matrix
        m, n = le.(matrix), le.(matrix[0])
        self.m, self.n = m, n
        __ not m or not n: r_
        self.tree = [[0]*(n+1) for _ in range(m+1)]
        self.nums = [[0]*n for _ in range(m)]
        for i in range(m
            for j in range(n
                self.update(i, j, matrix[i][j])
    
    ___ update(self, row, col, val
        m, n = self.m, self.n
        __ not m or not n: r_
        delta = val-self.nums[row][col]
        self.nums[row][col] = val
        i = 0
        w___ i < m+1:
            j = 0
            w___ j < n+1:
                self.tree[i][j] += delta
                j += j&(-1)
            i += i&(-i)
    
    ___ sumRegion(self, row1, col1, row2, col2
        m, n = self.m, self.n
        __ not m or not n:
            r_ 0
        r_ self.sumHelper(row2+1, col2+1)\
                +self.sumHelper(row1, col1)\
                -self.sumHelper(row1, col2+1)\
                -self.sumHelper(row2+1, col1)
        
    ___ sumHelper(self, row, col
        sumVal = 0
        i = row
        w___ i > 0:
            j = col
            w___ j > 0:
                sumVal += self.tree[i][j]
                j -= j&(-j)
            i -= i&(-i)
        r_ sumVal

class NumMatrix(object
    ___ __init__(self, matrix
        __ not matrix:
            r_
        self.matrix = matrix
        m, n = le.(matrix), le.(matrix[0])
        colSums = [[0]*n for _ in range(m+1)]
        for i in range(m+1
            for j in range(n
                colSums[i][j] = colSums[i-1][j] + matrix[i-1][j]
        self.colSums = colSums
    
    ___ update(self, row, col, val
        for i in range(row+1, le.(self.colSums)):
            self.colSums[i][col] = self.colSums[i][col]+val-self.matrix[row][col]
        self.matrix[row][col] = val
    
    ___ sumRegion(self, row1, col1, row2, col2
        result = 0
        for j in range(col1, col2+1
            result += self.colSums[row2+1][j] - self.colSums[row1][j]
        r_ result