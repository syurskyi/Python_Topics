class Solution(object):
  ___ pacificAtlantic(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    __ not matrix:
      return []
    n, m = len(matrix), len(matrix[0])
    pacific = set()
    atlantic = set()
    ans = []

    ___ dfs(matrix, visited, i, j):
      visited |= {(i, j)}
      for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ni, nj = i + di, j + dj
        __ 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
          __ matrix[ni][nj] >= matrix[i][j]:
            dfs(matrix, visited, ni, nj)

    for i in range(n):
      dfs(matrix, pacific, i, 0)
      dfs(matrix, atlantic, i, m - 1)
    for j in range(m):
      dfs(matrix, pacific, 0, j)
      dfs(matrix, atlantic, n - 1, j)
    return list(pacific & atlantic)
