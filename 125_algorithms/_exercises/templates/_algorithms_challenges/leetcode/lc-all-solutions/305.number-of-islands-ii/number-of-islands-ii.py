c_ UnionFind(o..
  ___ - , m, n
    dad [i ___ i __ r..(m * n)]
    rank [0 ___ _ __ r..(m * n)]

  ___ find  x
    __ dad[x] != x:
      dad[x] find(dad[x])
    r.. dad[x]

  ___ union  xy
    x, y map(find, xy)
    __ x __ y:
      r.. F..
    __ rank[x] > rank[y]:
      dad[y] x
    ____ rank[x] < rank[y]:
      dad[x] y
    ____
      dad[y] x
      rank[x] += 1
    r.. T..


c_ Solution(o..
  ___ numIslands2  m, n, positions
    """
    :type m: int
    :type n: int
    :type positions: List[List[int]]
    :rtype: List[int]
    """
    uf UnionFind(m, n)
    ans 0
    ret    # list
    dirs [(0, -1), (0, 1), (1, 0), (-1, 0)]
    grid s..()
    ___ i, j __ positions:
      ans += 1
      grid |= {(i, j)}
      ___ di, dj __ dirs:
        ni, nj i + di, j + dj
        __ 0 <_ ni < m a.. 0 <_ nj < n a.. (ni, nj) __ grid:
          __ uf.union((ni * n + nj, i * n + j:
            ans -_ 1
      ret.a..(ans)
    r.. ret
