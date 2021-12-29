class Solution(object):
  ___ pacificAtlantic(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    __ n.. matrix:
      r.. []
    n, m = l..(matrix), l..(matrix[0])
    pacific = set()
    atlantic = set()
    ans    # list

    ___ dfs(matrix, visited, i, j):
      visited |= {(i, j)}
      ___ di, dj __ [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ni, nj = i + di, j + dj
        __ 0 <= ni < n a.. 0 <= nj < m a.. (ni, nj) n.. __ visited:
          __ matrix[ni][nj] >= matrix[i][j]:
            dfs(matrix, visited, ni, nj)

    ___ i __ r..(n):
      dfs(matrix, pacific, i, 0)
      dfs(matrix, atlantic, i, m - 1)
    ___ j __ r..(m):
      dfs(matrix, pacific, 0, j)
      dfs(matrix, atlantic, n - 1, j)
    r.. l..(pacific & atlantic)
