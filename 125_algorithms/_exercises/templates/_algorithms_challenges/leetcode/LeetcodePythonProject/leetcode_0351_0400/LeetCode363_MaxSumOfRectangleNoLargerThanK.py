'''
Created on Mar 27, 2017

@author: MT
'''

class Solution(object
    ___ maxSumSubmatrix(self, matrix, k
        pass
    
    # still not working!
    ___ maxSumSubmatrixBinarySearch(self, matrix, k
        ______ bisect
        __ not matrix or not matrix[0]:
            r_ 0
        m, n = le.(matrix), le.(matrix[0])
        areas = [[0]*n ___ _ in range(m)]
        ___ i in range(m
            ___ j in range(n
                __ i __ 0 and j __ 0: areas[i][j] = matrix[i][j]
                __ i __ 0 and j != 0: areas[i][j] = matrix[i][j]+areas[i][j-1]
                __ i != 0 and j __ 0: areas[i][j] = matrix[i][j]+areas[i-1][j]
                __ i != 0 and j != 0:
                    areas[i][j] = areas[i][j-1]+areas[i-1][j]+areas[i-1][j-1]+matrix[i][j]
        maxVal = float('-inf')
        ___ r1 in range(m
            ___ r2 in range(r1, m
                sortedlist = [0]
                ___ c in range(n
                    area = areas[r2][c]
                    __ r1-1>=0:
                        area -= areas[r2][c]
                    ind = bisect.bisect_left(sortedlist, area-k)
                    __ ind < le.(sortedlist
                        maxVal = max(maxVal, area-sortedlist[ind])
                    bisect.insort_left(sortedlist, area)
        r_ maxVal
