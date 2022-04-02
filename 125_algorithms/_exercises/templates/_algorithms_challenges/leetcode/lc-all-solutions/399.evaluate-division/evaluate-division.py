____ c.. _______ d..


c_ Graph(o..
  ___ -
    graph    # dict

  ___ get  label
    __ label n.. __ graph:
      graph[label] = GraphNode(label)
    r.. graph[label]

  ___ query  node1, node2
    g = graph
    __ l..(node1.nbrs) __ 0 o. l..(node2.nbrs) __ 0:
      r.. -1.0
    __ node1 __ node2:
      r.. 1.0
    queue = d..([(node1, 1)])
    visited = s..([node1.label])
    w.... queue:
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

  ___ connect  node1, node2, div
    node1.nbrs[node2.label] = div
    __ div != 0:
      node2.nbrs[node1.label] = 1.0 / div
    ____:
      node2.nbrs[node1.label] = f__("inf")


c_ GraphNode(o..
  ___ - , label
    label = label
    nbrs    # dict


c_ Solution(o..
  ___ calcEquation  equations, values, queries
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    visited    # dict
    g = Graph()
    ans    # list
    ___ i __ r..(0, l..(equations)):
      label1, label2 = equations[i]
      node1, node2 = g.get(label1), g.get(label2)
      g.connect(node1, node2, values[i])

    ___ query __ queries:
      ans.a..(g.query(g.get(query[0]), g.get(query[1])))
    r.. ans
