class Solution(object
  ___ countComponents(self, n, edges
    ___ find(x
      __ parent[x] != x:
        parent[x] = find(parent[x])
      r_ parent[x]

    ___ union(xy
      x, y = map(find, xy)
      __ rank[x] > rank[y]:
        parent[y] = x
      ____
        parent[x] = y
        __ rank[x] __ rank[y]:
          rank[y] += 1

    parent, rank = range(n), [0] * n
    map(union, edges)
    r_ le.({find(x) for x in parent})
