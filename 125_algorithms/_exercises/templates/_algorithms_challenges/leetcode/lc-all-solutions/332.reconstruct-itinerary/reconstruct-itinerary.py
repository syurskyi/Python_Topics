____ collections _______ deque


class Solution(object):
  ___ findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = {}
    hashset = set([])
    ___ ticket __ tickets:
      graph[ticket[0]] = graph.get(ticket[0], []) + [ticket[1]]

    maxLen = l..(tickets) + 1

    ___ k __ graph:
      graph[k] = deque(s..(graph[k]))

    ___ dfs(path, graph, maxLen, start):
      __ l..(path) __ maxLen:
        r.. path + []
      ___ k __ r..(0, l..(graph.get(start, []))):
        nbr = graph.get(start, [])
        top = nbr.popleft()
        path.a..(top)
        ret = dfs(path, graph, maxLen, top)
        __ ret:
          r.. ret
        path.pop()
        nbr.a..(top)
      r.. []

    r.. dfs(["JFK"], graph, maxLen, "JFK")
