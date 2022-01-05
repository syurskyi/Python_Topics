c_ UnionFind(object):
  ___ - , n):
    dad = [i ___ i __ r..(n)]
    rank = [0 ___ i __ r..(n)]
    count = n

  ___ find  x):
    dad = dad
    __ dad[x] != x:
      dad[x] = find(dad[x])
    r.. dad[x]

  ___ union  x, y):
    dad = dad
    rank = rank
    x, y = map(find, [x, y])
    __ x __ y:
      r.. F..
    __ rank[x] > rank[y]:
      dad[y] = x
    ____:
      dad[x] = y
      __ rank[x] __ rank[y]:
        rank[y] += 1
    count -= 1
    r.. T..

  ___ getCount
    r.. count


c_ Solution(object):
  ___ findCircleNum  M):
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
