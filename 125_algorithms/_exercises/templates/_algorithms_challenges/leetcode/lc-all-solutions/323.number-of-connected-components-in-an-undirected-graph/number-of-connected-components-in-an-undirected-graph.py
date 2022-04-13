c_ Solution(o..
  ___ countComponents  n, edges
    ___ find(x
      __ parent[x] !_ x:
        parent[x] find(parent[x])
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
    r.. l..({find(x) ___ x __ parent})
