'''
Created on Mar 13, 2017

@author: MT
'''
c_ NumMatrix_BinaryIndexTree_TLE(o..
    ___ - , matrix
        m, n = l..(matrix), l..(matrix[0])
        m, n = m, n
        __ n.. m o. n.. n: r..
        tree = [[0]*(n+1) ___ _ __ r..(m+1)]
        nums = [[0]*n ___ _ __ r..(m)]
        ___ i __ r..(m
            ___ j __ r..(n
                update(i, j, matrix[i][j])
    
    ___ update  row, col, val
        m, n = m, n
        __ n.. m o. n.. n: r..
        delta = val-nums[row][col]
        nums[row][col] = val
        i = 0
        w.... i < m+1:
            j = 0
            w.... j < n+1:
                tree[i][j] += delta
                j += j&(-1)
            i += i&(-i)
    
    ___ sumRegion  row1, col1, row2, col2
        m, n = m, n
        __ n.. m o. n.. n:
            r.. 0
        r.. sumHelper(row2+1, col2+1)\
                +sumHelper(row1, col1)\
                -sumHelper(row1, col2+1)\
                -sumHelper(row2+1, col1)
        
    ___ sumHelper  row, col
        sumVal = 0
        i = row
        w.... i > 0:
            j = col
            w.... j > 0:
                sumVal += tree[i][j]
                j -= j&(-j)
            i -= i&(-i)
        r.. sumVal

c_ NumMatrix(o..
    ___ - , matrix
        __ n.. matrix:
            r..
        matrix = matrix
        m, n = l..(matrix), l..(matrix[0])
        colSums = [[0]*n ___ _ __ r..(m+1)]
        ___ i __ r..(m+1
            ___ j __ r..(n
                colSums[i][j] = colSums[i-1][j] + matrix[i-1][j]
        colSums = colSums
    
    ___ update  row, col, val
        ___ i __ r..(row+1, l..(colSums:
            colSums[i][col] = colSums[i][col]+val-matrix[row][col]
        matrix[row][col] = val
    
    ___ sumRegion  row1, col1, row2, col2
        result = 0
        ___ j __ r..(col1, col2+1
            result += colSums[row2+1][j] - colSums[row1][j]
        r.. result