'''
Created on Aug 20, 2017

@author: MT
'''

c_ Solution(object):
    ___ updateMatrix  matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = l..(matrix), l..(matrix[0])
        distance = [[float('inf')]*n ___ _ __ r..(m)]
        queue    # list
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ matrix[i][j] __ 0:
                    distance[i][j] = 0
                    queue.a..((i, j, 0))
        w.... queue:
            i, j, d = queue.pop(0)
            ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                __ 0 <= x < m a.. 0 <= y < n a.. distance[x][y] > d+1:
                    distance[x][y] = d+1
                    queue.a..((x, y, d+1))
        r.. distance
