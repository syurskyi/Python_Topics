'''
Created on Aug 20, 2017

@author: MT
'''

class Solution(object
    ___ updateMatrix(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = le.(matrix), le.(matrix[0])
        distance = [[float('inf')]*n ___ _ in range(m)]
        queue = []
        ___ i in range(m
            ___ j in range(n
                __ matrix[i][j] __ 0:
                    distance[i][j] = 0
                    queue.append((i, j, 0))
        w___ queue:
            i, j, d = queue.pop(0)
            ___ x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1
                __ 0 <= x < m and 0 <= y < n and distance[x][y] > d+1:
                    distance[x][y] = d+1
                    queue.append((x, y, d+1))
        r_ distance
