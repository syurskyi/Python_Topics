'''
Created on Mar 27, 2017

@author: MT
'''

class Solution(object):
    ___ maxSumSubmatrix(self, matrix, k):
        pass
    
    # still not working!
    ___ maxSumSubmatrixBinarySearch(self, matrix, k):
        import bisect
        __ not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        areas = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                __ i == 0 and j == 0: areas[i][j] = matrix[i][j]
                __ i == 0 and j != 0: areas[i][j] = matrix[i][j]+areas[i][j-1]
                __ i != 0 and j == 0: areas[i][j] = matrix[i][j]+areas[i-1][j]
                __ i != 0 and j != 0:
                    areas[i][j] = areas[i][j-1]+areas[i-1][j]+areas[i-1][j-1]+matrix[i][j]
        maxVal = float('-inf')
        for r1 in range(m):
            for r2 in range(r1, m):
                sortedlist = [0]
                for c in range(n):
                    area = areas[r2][c]
                    __ r1-1>=0:
                        area -= areas[r2][c]
                    ind = bisect.bisect_left(sortedlist, area-k)
                    __ ind < len(sortedlist):
                        maxVal = max(maxVal, area-sortedlist[ind])
                    bisect.insort_left(sortedlist, area)
        return maxVal
