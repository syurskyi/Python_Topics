class UnionFind(object):
  ___ __init__(self, m, n):
    self.dad = [i for i in range(m * n)]
    self.rank = [0 for _ in range(m * n)]

  ___ find(self, x):
    __ self.dad[x] != x:
      self.dad[x] = self.find(self.dad[x])
    return self.dad[x]

  ___ union(self, xy):
    x, y = map(self.find, xy)
    __ x == y:
      return False
    __ self.rank[x] > self.rank[y]:
      self.dad[y] = x
    elif self.rank[x] < self.rank[y]:
      self.dad[x] = y
    else:
      self.dad[y] = x
      self.rank[x] += 1
    return True


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
    ret = []
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    grid = set()
    for i, j in positions:
      ans += 1
      grid |= {(i, j)}
      for di, dj in dirs:
        ni, nj = i + di, j + dj
        __ 0 <= ni < m and 0 <= nj < n and (ni, nj) in grid:
          __ uf.union((ni * n + nj, i * n + j)):
            ans -= 1
      ret.append(ans)
    return ret
