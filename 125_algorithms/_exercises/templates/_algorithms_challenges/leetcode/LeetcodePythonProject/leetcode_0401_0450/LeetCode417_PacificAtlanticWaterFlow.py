'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object
    ___ pacificAtlantic(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ not matrix or not matrix[0]: r_   # list
        m, n = le.(matrix), le.(matrix[0])
        pacific = [[False]*n ___ _ __ range(m)]
        atlantic = [[False]*n ___ _ __ range(m)]
        ___ i __ range(m
            self.dfs(matrix, i, 0, pacific)
            self.dfs(matrix, i, n-1, atlantic)
        ___ j __ range(n
            self.dfs(matrix, 0, j, pacific)
            self.dfs(matrix, m-1, j, atlantic)
        result =   # list
        ___ i __ range(m
            ___ j __ range(n
                __ pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        r_ result
    
    ___ dfs(self, matrix, i, j, visited
        visited[i][j] = True
        m, n = le.(matrix), le.(matrix[0])
        ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1
            __ 0 <= x < m and 0 <= y < n and\
                not visited[x][y] and matrix[x][y] >= matrix[i][j]:
                self.dfs(matrix, x, y, visited)
