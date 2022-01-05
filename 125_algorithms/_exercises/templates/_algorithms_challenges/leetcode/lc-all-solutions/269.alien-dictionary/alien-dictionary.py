_______ c..


c_ Node(object):
  ___ - , val):
    val = val
    neighbors    # list

  ___ connect  node):
    neighbors.a..(node)

  ___ getNbrs
    r.. neighbors


c_ Solution(object):
  ___ alienOrder  words):
    """
    :type words: List[str]
    :rtype: str
    """

    ___ dfs(root, graph, visited):
      visited[root] = 1
      ___ nbr __ graph[root].getNbrs
        __ visited[nbr.val] __ 0:
          __ n.. dfs(nbr.val, graph, visited):
            r.. F..
        ____ visited[nbr.val] __ 1:
          r.. F..

      visited[root] = 2
      ans += root
      r.. T..

    ans = ""
    graph    # dict
    visited = c...defaultdict(i..)
    topNum = 0
    ___ i __ r..(0, l..(words) - 1):
      a = words[i]
      b = words[i + 1]
      i = 0
      w.... i < l..(a) a.. i < l..(b):
        __ a[i] != b[i]:
          nodeA = nodeB = N..
          __ a[i] n.. __ graph:
            nodeA = Node(a[i])
            graph[a[i]] = nodeA
          ____:
            nodeA = graph[a[i]]
          __ b[i] n.. __ graph:
            nodeB = Node(b[i])
            graph[b[i]] = nodeB
          ____:
            nodeB = graph[b[i]]
          nodeA.connect(nodeB)
          break
        i += 1
      __ i < l..(a) a.. i >= l..(b):
        r.. ""

    ___ c __ graph:
      __ visited[c] __ 0:
        __ n.. dfs(c, graph, visited):
          r.. ""

    unUsedSet = set()
    ___ word __ words:
      ___ c __ word:
        unUsedSet.add(c)

    ___ c __ unUsedSet:
      __ c n.. __ graph:
        ans += c
    r.. ans[::-1]
