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
        __ not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        pacific = [[False]*n for _ in range(m)]
        atlantic = [[False]*n for _ in range(m)]
        for i in range(m):
            self.dfs(matrix, i, 0, pacific)
            self.dfs(matrix, i, n-1, atlantic)
        for j in range(n):
            self.dfs(matrix, 0, j, pacific)
            self.dfs(matrix, m-1, j, atlantic)
        result = []
        for i in range(m):
            for j in range(n):
                __ pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result
    
    ___ dfs(self, matrix, i, j, visited):
        visited[i][j] = True
        m, n = len(matrix), len(matrix[0])
        for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            __ 0 <= x < m and 0 <= y < n and\
                not visited[x][y] and matrix[x][y] >= matrix[i][j]:
                self.dfs(matrix, x, y, visited)
