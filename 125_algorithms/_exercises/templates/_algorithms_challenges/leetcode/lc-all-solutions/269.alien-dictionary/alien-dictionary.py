______ collections


class Node(object
  ___ __init__(self, val
    self.val = val
    self.neighbors = []

  ___ connect(self, node
    self.neighbors.append(node)

  ___ getNbrs(self
    r_ self.neighbors


class Solution(object
  ___ alienOrder(self, words
    """
    :type words: List[str]
    :rtype: str
    """

    ___ dfs(root, graph, visited
      visited[root] = 1
      for nbr in graph[root].getNbrs(
        __ visited[nbr.val] __ 0:
          __ not dfs(nbr.val, graph, visited
            r_ False
        ____ visited[nbr.val] __ 1:
          r_ False

      visited[root] = 2
      self.ans += root
      r_ True

    self.ans = ""
    graph = {}
    visited = collections.defaultdict(int)
    self.topNum = 0
    for i in range(0, le.(words) - 1
      a = words[i]
      b = words[i + 1]
      i = 0
      w___ i < le.(a) and i < le.(b
        __ a[i] != b[i]:
          nodeA = nodeB = None
          __ a[i] not in graph:
            nodeA = Node(a[i])
            graph[a[i]] = nodeA
          ____
            nodeA = graph[a[i]]
          __ b[i] not in graph:
            nodeB = Node(b[i])
            graph[b[i]] = nodeB
          ____
            nodeB = graph[b[i]]
          nodeA.connect(nodeB)
          break
        i += 1
      __ i < le.(a) and i >= le.(b
        r_ ""

    for c in graph:
      __ visited[c] __ 0:
        __ not dfs(c, graph, visited
          r_ ""

    unUsedSet = set()
    for word in words:
      for c in word:
        unUsedSet.add(c)

    for c in unUsedSet:
      __ c not in graph:
        self.ans += c
    r_ self.ans[::-1]
