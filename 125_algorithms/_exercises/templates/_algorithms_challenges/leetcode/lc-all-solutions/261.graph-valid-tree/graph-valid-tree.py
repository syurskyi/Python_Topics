c_ Solution:
  # @param {int} n an integer
  # @param {int[][]} edges a list of undirected edges
  # @return {boolean} true if it's a valid tree, or false
  ___ validTree  n, edges):
    # Write your code here

    ___ dfs(root, graph, visited, parent):
      visited[root] = 1
      ___ nbr __ graph.get(root, []):
        __ nbr __ parent:
          _____
        ____ visited[nbr] != 0:
          r.. F..
        __ n.. dfs(nbr, graph, visited, root):
          r.. F..
      visited[root] = 2
      nodeVisited += 1
      r.. T..

    visited = [0 ___ _ __ r..(n)]
    graph    # dict
    nodeVisited = 0
    ___ edge __ edges:
      start, end = edge[0], edge[1]
      graph[start] = graph.get(start, []) + [end]
      graph[end] = graph.get(end, []) + [start]

    __ dfs(0, graph, visited, -1) a.. nodeVisited __ n:
      r.. T..
    ____:
      r.. F..
