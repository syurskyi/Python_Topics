# Definition for a undirected graph node
# class UndirectedGraphNode:
#     ___ __init__(self, x
#         self.label = x
#         self.neighbors = []

class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  ___ cloneGraph(self, node
    graph = {}
    visited = set()

    ___ dfs(node, visited, graph
      __ not node or node.label __ visited:
        r_
      visited |= {node.label}
      __ node.label not __ graph:
        graph[node.label] = UndirectedGraphNode(node.label)
      newNode = graph[node.label]

      ___ nbr __ node.neighbors:
        __ nbr.label not __ graph:
          graph[nbr.label] = UndirectedGraphNode(nbr.label)
        newNode.neighbors.append(graph[nbr.label])
        dfs(nbr, visited, graph)
      r_ newNode

    r_ dfs(node, visited, graph)
