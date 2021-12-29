class Solution:
  # @param {int} n an integer
  # @param {int[][]} edges a list of undirected edges
  # @return {boolean} true if it's a valid tree, or false
  ___ validTree(self, n, edges):
    # Write your code here

    ___ dfs(root, graph, visited, parent):
      visited[root] = 1
      for nbr in graph.get(root, []):
        __ nbr == parent:
          continue
        elif visited[nbr] != 0:
          return False
        __ not dfs(nbr, graph, visited, root):
          return False
      visited[root] = 2
      self.nodeVisited += 1
      return True

    visited = [0 for _ in range(n)]
    graph = {}
    self.nodeVisited = 0
    for edge in edges:
      start, end = edge[0], edge[1]
      graph[start] = graph.get(start, []) + [end]
      graph[end] = graph.get(end, []) + [start]

    __ dfs(0, graph, visited, -1) and self.nodeVisited == n:
      return True
    else:
      return False
