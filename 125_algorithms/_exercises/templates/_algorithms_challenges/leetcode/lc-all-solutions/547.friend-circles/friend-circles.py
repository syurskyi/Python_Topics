class UnionFind(object):
  ___ __init__(self, n):
    self.dad = [i ___ i __ r..(n)]
    self.rank = [0 ___ i __ r..(n)]
    self.count = n

  ___ find(self, x):
    dad = self.dad
    __ dad[x] != x:
      dad[x] = self.find(dad[x])
    r.. dad[x]

  ___ union(self, x, y):
    dad = self.dad
    rank = self.rank
    x, y = map(self.find, [x, y])
    __ x __ y:
      r.. False
    __ rank[x] > rank[y]:
      dad[y] = x
    ____:
      dad[x] = y
      __ rank[x] __ rank[y]:
        rank[y] += 1
    self.count -= 1
    r.. True

  ___ getCount(self):
    r.. self.count


class Solution(object):
  ___ findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    uf = UnionFind(l..(M))
    ans = 0
    ___ i __ r..(l..(M)):
      ___ j __ r..(l..(M[0])):
        __ M[i][j] __ 1:
          uf.union(i, j)
    r.. uf.getCount()
