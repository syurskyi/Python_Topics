class Solution(object
  ___ imageSmoother(self, M
    """
    :type M: List[List[int]]
    :rtype: List[List[int]]
    """
    m = le.(M)
    n = le.(M[0])
    ans = [[0] * n ___ _ in range(m)]

    ___ i in range(m
      ___ j in range(n
        cnt = 0
        sums = 0
        ___ di in range(-1, 2
          ___ dj in range(-1, 2
            newi, newj = i + di, j + dj
            __ 0 <= newi < m and 0 <= newj < n:
              cnt += 1
              sums += M[newi][newj]
        ans[i][j] = sums / cnt
    r_ ans
