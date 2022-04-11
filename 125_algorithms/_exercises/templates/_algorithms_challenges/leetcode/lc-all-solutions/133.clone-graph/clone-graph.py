# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

c_ Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  ___ cloneGraph  node
    graph    # dict
    visited s..()

    ___ dfs(node, visited, graph
      __ n.. node o. node.label __ visited:
        r..
      visited |= {node.label}
      __ node.label n.. __ graph:
        graph[node.label] UndirectedGraphNode(node.label)
      newNode graph[node.label]

      ___ nbr __ node.neighbors:
        __ nbr.label n.. __ graph:
          graph[nbr.label] UndirectedGraphNode(nbr.label)
        newNode.neighbors.a..(graph[nbr.label])
        dfs(nbr, visited, graph)
      r.. newNode

    r.. dfs(node, visited, graph)
