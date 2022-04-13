c_ Solution(o..
  ___ countComponents  n, edges
    ___ f.. x
      __ parent[x] !_ x:
        parent[x] f.. parent[x])
      r.. parent[x]

    ___ union(xy
      x, y m.. find, xy)
      __ rank[x] > rank[y]:
        parent[y] x
      ____
        parent[x] y
        __ rank[x] __ rank[y]:
          rank[y] += 1

    parent, rank r..(n), [0] * n
    m.. union, edges)
    r.. l..({f.. x) ___ x __ parent})
