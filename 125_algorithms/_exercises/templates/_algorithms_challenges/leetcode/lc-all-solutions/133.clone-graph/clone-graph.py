# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  ___ cloneGraph(self, node):
    graph = {}
    visited = set()

    ___ dfs(node, visited, graph):
      __ not node or node.label in visited:
        return
      visited |= {node.label}
      __ node.label not in graph:
        graph[node.label] = UndirectedGraphNode(node.label)
      newNode = graph[node.label]

      for nbr in node.neighbors:
        __ nbr.label not in graph:
          graph[nbr.label] = UndirectedGraphNode(nbr.label)
        newNode.neighbors.append(graph[nbr.label])
        dfs(nbr, visited, graph)
      return newNode

    return dfs(node, visited, graph)
