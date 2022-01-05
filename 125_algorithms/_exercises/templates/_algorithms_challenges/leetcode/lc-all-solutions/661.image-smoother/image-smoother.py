c_ Solution(o..):
  ___ imageSmoother  M):
    """
    :type M: List[List[int]]
    :rtype: List[List[int]]
    """
    m = l..(M)
    n = l..(M[0])
    ans = [[0] * n ___ _ __ r..(m)]

    ___ i __ r..(m):
      ___ j __ r..(n):
        cnt = 0
        sums = 0
        ___ di __ r..(-1, 2):
          ___ dj __ r..(-1, 2):
            newi, newj = i + di, j + dj
            __ 0 <= newi < m a.. 0 <= newj < n:
              cnt += 1
              sums += M[newi][newj]
        ans[i][j] = sums / cnt
    r.. ans
