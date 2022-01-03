'''
Created on Mar 27, 2017

@author: MT
'''

c_ Solution(object):
    ___ maxSumSubmatrix(self, matrix, k):
        pass
    
    # still not working!
    ___ maxSumSubmatrixBinarySearch(self, matrix, k):
        _______ bisect
        __ n.. matrix o. n.. matrix[0]:
            r.. 0
        m, n = l..(matrix), l..(matrix[0])
        areas = [[0]*n ___ _ __ r..(m)]
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ i __ 0 a.. j __ 0: areas[i][j] = matrix[i][j]
                __ i __ 0 a.. j != 0: areas[i][j] = matrix[i][j]+areas[i][j-1]
                __ i != 0 a.. j __ 0: areas[i][j] = matrix[i][j]+areas[i-1][j]
                __ i != 0 a.. j != 0:
                    areas[i][j] = areas[i][j-1]+areas[i-1][j]+areas[i-1][j-1]+matrix[i][j]
        maxVal = float('-inf')
        ___ r1 __ r..(m):
            ___ r2 __ r..(r1, m):
                sortedlist = [0]
                ___ c __ r..(n):
                    area = areas[r2][c]
                    __ r1-1>=0:
                        area -= areas[r2][c]
                    ind = bisect.bisect_left(sortedlist, area-k)
                    __ ind < l..(sortedlist):
                        maxVal = max(maxVal, area-sortedlist[ind])
                    bisect.insort_left(sortedlist, area)
        r.. maxVal
