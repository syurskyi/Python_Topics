class Solution(object
  ___ longestLine(self, M
    """
    :type M: List[List[int]]
    :rtype: int
    """
    __ not M:
      r_ 0
    hor = [[0] * (le.(M[0]) + 2) ___ _ in range(le.(M) + 1)]
    ver = [[0] * (le.(M[0]) + 2) ___ _ in range(le.(M) + 1)]
    diag = [[0] * (le.(M[0]) + 2) ___ _ in range(le.(M) + 1)]
    anti = [[0] * (le.(M[0]) + 2) ___ _ in range(le.(M) + 1)]
    ans = 0
    ___ i in range(le.(M)):
      ___ j in range(le.(M[0])):
        __ M[i][j] __ 1:
          hor[i + 1][j + 1] = hor[i + 1][j] + 1
          ver[i + 1][j + 1] = ver[i][j + 1] + 1
          diag[i + 1][j + 1] = diag[i][j] + 1
          anti[i + 1][j + 1] = anti[i][j + 2] + 1
          ans = max(ans, hor[i + 1][j + 1], ver[i + 1][j + 1], diag[i + 1][j + 1], anti[i + 1][j + 1])
    r_ ans
