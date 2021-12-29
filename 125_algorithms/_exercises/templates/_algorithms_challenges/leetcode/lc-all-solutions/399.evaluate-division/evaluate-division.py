from collections import deque


class Graph(object):
  ___ __init__(self):
    self.graph = {}

  ___ get(self, label):
    __ label not in self.graph:
      self.graph[label] = GraphNode(label)
    return self.graph[label]

  ___ query(self, node1, node2):
    g = self.graph
    __ len(node1.nbrs) == 0 or len(node2.nbrs) == 0:
      return -1.0
    __ node1 == node2:
      return 1.0
    queue = deque([(node1, 1)])
    visited = set([node1.label])
    while queue:
      node, ans = queue.popleft()
      for nbr in node.nbrs:
        __ nbr not in visited:
          w = node.nbrs[nbr]
          visited |= {nbr}
          nbrNode = g.get(nbr)
          __ nbrNode == node2:
            return ans * w
          queue.append((nbrNode, ans * w))

    return -1.0

  ___ connect(self, node1, node2, div):
    node1.nbrs[node2.label] = div
    __ div != 0:
      node2.nbrs[node1.label] = 1.0 / div
    else:
      node2.nbrs[node1.label] = float("inf")


class GraphNode(object):
  ___ __init__(self, label):
    self.label = label
    self.nbrs = {}


class Solution(object):
  ___ calcEquation(self, equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    visited = {}
    g = Graph()
    ans = []
    for i in range(0, len(equations)):
      label1, label2 = equations[i]
      node1, node2 = g.get(label1), g.get(label2)
      g.connect(node1, node2, values[i])

    for query in queries:
      ans.append(g.query(g.get(query[0]), g.get(query[1])))
    return ans
