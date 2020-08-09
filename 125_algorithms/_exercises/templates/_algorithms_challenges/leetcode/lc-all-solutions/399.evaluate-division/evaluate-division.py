from collections ______ deque


class Graph(object
  ___ __init__(self
    self.graph = {}

  ___ get(self, label
    __ label not in self.graph:
      self.graph[label] = GraphNode(label)
    r_ self.graph[label]

  ___ query(self, node1, node2
    g = self.graph
    __ le.(node1.nbrs) __ 0 or le.(node2.nbrs) __ 0:
      r_ -1.0
    __ node1 __ node2:
      r_ 1.0
    queue = deque([(node1, 1)])
    visited = set([node1.label])
    w___ queue:
      node, ans = queue.popleft()
      ___ nbr in node.nbrs:
        __ nbr not in visited:
          w = node.nbrs[nbr]
          visited |= {nbr}
          nbrNode = g.get(nbr)
          __ nbrNode __ node2:
            r_ ans * w
          queue.append((nbrNode, ans * w))

    r_ -1.0

  ___ connect(self, node1, node2, div
    node1.nbrs[node2.label] = div
    __ div != 0:
      node2.nbrs[node1.label] = 1.0 / div
    ____
      node2.nbrs[node1.label] = float("inf")


class GraphNode(object
  ___ __init__(self, label
    self.label = label
    self.nbrs = {}


class Solution(object
  ___ calcEquation(self, equations, values, queries
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    visited = {}
    g = Graph()
    ans = []
    ___ i in range(0, le.(equations)):
      label1, label2 = equations[i]
      node1, node2 = g.get(label1), g.get(label2)
      g.connect(node1, node2, values[i])

    ___ query in queries:
      ans.append(g.query(g.get(query[0]), g.get(query[1])))
    r_ ans
