class Solution:
  # @param {int} n an integer
  # @param {int[][]} edges a list of undirected edges
  # @return {boolean} true if it's a valid tree, or false
  ___ validTree(self, n, edges
    # Write your code here

    ___ dfs(root, graph, visited, parent
      visited[root] = 1
      ___ nbr in graph.get(root, []
        __ nbr __ parent:
          continue
        ____ visited[nbr] != 0:
          r_ False
        __ not dfs(nbr, graph, visited, root
          r_ False
      visited[root] = 2
      self.nodeVisited += 1
      r_ True

    visited = [0 ___ _ in range(n)]
    graph = {}
    self.nodeVisited = 0
    ___ edge in edges:
      start, end = edge[0], edge[1]
      graph[start] = graph.get(start, []) + [end]
      graph[end] = graph.get(end, []) + [start]

    __ dfs(0, graph, visited, -1) and self.nodeVisited __ n:
      r_ True
    ____
      r_ False
