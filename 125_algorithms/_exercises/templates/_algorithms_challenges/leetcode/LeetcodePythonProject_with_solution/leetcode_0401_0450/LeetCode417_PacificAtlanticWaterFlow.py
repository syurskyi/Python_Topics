'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object):
    ___ pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]: r.. []
        m, n = l..(matrix), l..(matrix[0])
        pacific = [[False]*n ___ _ __ r..(m)]
        atlantic = [[False]*n ___ _ __ r..(m)]
        ___ i __ r..(m):
            self.dfs(matrix, i, 0, pacific)
            self.dfs(matrix, i, n-1, atlantic)
        ___ j __ r..(n):
            self.dfs(matrix, 0, j, pacific)
            self.dfs(matrix, m-1, j, atlantic)
        result    # list
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ pacific[i][j] a.. atlantic[i][j]:
                    result.a..([i, j])
        r.. result
    
    ___ dfs(self, matrix, i, j, visited):
        visited[i][j] = True
        m, n = l..(matrix), l..(matrix[0])
        ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            __ 0 <= x < m a.. 0 <= y < n a..\
                n.. visited[x][y] a.. matrix[x][y] >= matrix[i][j]:
                self.dfs(matrix, x, y, visited)
