class Solution(object
  ___ pacificAtlantic(self, matrix
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    __ not matrix:
      r_   # list
    n, m = le.(matrix), le.(matrix[0])
    pacific = set()
    atlantic = set()
    ans =   # list

    ___ dfs(matrix, visited, i, j
      visited |= {(i, j)}
      ___ di, dj __ [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ni, nj = i + di, j + dj
        __ 0 <= ni < n and 0 <= nj < m and (ni, nj) not __ visited:
          __ matrix[ni][nj] >= matrix[i][j]:
            dfs(matrix, visited, ni, nj)

    ___ i __ range(n
      dfs(matrix, pacific, i, 0)
      dfs(matrix, atlantic, i, m - 1)
    ___ j __ range(m
      dfs(matrix, pacific, 0, j)
      dfs(matrix, atlantic, n - 1, j)
    r_ list(pacific & atlantic)
