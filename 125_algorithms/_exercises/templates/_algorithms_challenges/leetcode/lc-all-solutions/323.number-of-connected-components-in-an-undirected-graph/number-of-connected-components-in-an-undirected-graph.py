class Solution(object):
  ___ countComponents(self, n, edges):
    ___ find(x):
      __ parent[x] != x:
        parent[x] = find(parent[x])
      return parent[x]

    ___ union(xy):
      x, y = map(find, xy)
      __ rank[x] > rank[y]:
        parent[y] = x
      else:
        parent[x] = y
        __ rank[x] == rank[y]:
          rank[y] += 1

    parent, rank = range(n), [0] * n
    map(union, edges)
    return len({find(x) for x in parent})
