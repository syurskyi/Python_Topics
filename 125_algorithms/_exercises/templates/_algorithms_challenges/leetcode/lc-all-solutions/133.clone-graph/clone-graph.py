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
      __ not node or node.label in visited:
        r_
      visited |= {node.label}
      __ node.label not in graph:
        graph[node.label] = UndirectedGraphNode(node.label)
      newNode = graph[node.label]

      ___ nbr in node.neighbors:
        __ nbr.label not in graph:
          graph[nbr.label] = UndirectedGraphNode(nbr.label)
        newNode.neighbors.append(graph[nbr.label])
        dfs(nbr, visited, graph)
      r_ newNode

    r_ dfs(node, visited, graph)
