class UnionFind(object):
  ___ __init__(self, m, n):
    self.dad = [i ___ i __ r..(m * n)]
    self.rank = [0 ___ _ __ r..(m * n)]

  ___ find(self, x):
    __ self.dad[x] != x:
      self.dad[x] = self.find(self.dad[x])
    r.. self.dad[x]

  ___ union(self, xy):
    x, y = map(self.find, xy)
    __ x __ y:
      r.. False
    __ self.rank[x] > self.rank[y]:
      self.dad[y] = x
    ____ self.rank[x] < self.rank[y]:
      self.dad[x] = y
    ____:
      self.dad[y] = x
      self.rank[x] += 1
    r.. True


class Solution(object):
  ___ numIslands2(self, m, n, positions):
    """
    :type m: int
    :type n: int
    :type positions: List[List[int]]
    :rtype: List[int]
    """
    uf = UnionFind(m, n)
    ans = 0
    ret    # list
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    grid = set()
    ___ i, j __ positions:
      ans += 1
      grid |= {(i, j)}
      ___ di, dj __ dirs:
        ni, nj = i + di, j + dj
        __ 0 <= ni < m and 0 <= nj < n and (ni, nj) __ grid:
          __ uf.union((ni * n + nj, i * n + j)):
            ans -= 1
      ret.a..(ans)
    r.. ret
