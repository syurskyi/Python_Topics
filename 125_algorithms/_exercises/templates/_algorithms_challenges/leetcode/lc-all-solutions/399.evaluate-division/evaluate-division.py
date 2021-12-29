____ collections _______ deque


class Graph(object):
  ___ __init__(self):
    self.graph = {}

  ___ get(self, label):
    __ label n.. __ self.graph:
      self.graph[label] = GraphNode(label)
    r.. self.graph[label]

  ___ query(self, node1, node2):
    g = self.graph
    __ l..(node1.nbrs) __ 0 o. l..(node2.nbrs) __ 0:
      r.. -1.0
    __ node1 __ node2:
      r.. 1.0
    queue = deque([(node1, 1)])
    visited = set([node1.label])
    while queue:
      node, ans = queue.popleft()
      ___ nbr __ node.nbrs:
        __ nbr n.. __ visited:
          w = node.nbrs[nbr]
          visited |= {nbr}
          nbrNode = g.get(nbr)
          __ nbrNode __ node2:
            r.. ans * w
          queue.a..((nbrNode, ans * w))

    r.. -1.0

  ___ connect(self, node1, node2, div):
    node1.nbrs[node2.label] = div
    __ div != 0:
      node2.nbrs[node1.label] = 1.0 / div
    ____:
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
    ans    # list
    ___ i __ r..(0, l..(equations)):
      label1, label2 = equations[i]
      node1, node2 = g.get(label1), g.get(label2)
      g.connect(node1, node2, values[i])

    ___ query __ queries:
      ans.a..(g.query(g.get(query[0]), g.get(query[1])))
    r.. ans
