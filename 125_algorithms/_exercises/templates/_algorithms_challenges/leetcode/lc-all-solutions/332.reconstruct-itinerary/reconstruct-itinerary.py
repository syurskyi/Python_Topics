from collections import deque


class Solution(object):
  ___ findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = {}
    hashset = set([])
    for ticket in tickets:
      graph[ticket[0]] = graph.get(ticket[0], []) + [ticket[1]]

    maxLen = len(tickets) + 1

    for k in graph:
      graph[k] = deque(sorted(graph[k]))

    ___ dfs(path, graph, maxLen, start):
      __ len(path) == maxLen:
        return path + []
      for k in range(0, len(graph.get(start, []))):
        nbr = graph.get(start, [])
        top = nbr.popleft()
        path.append(top)
        ret = dfs(path, graph, maxLen, top)
        __ ret:
          return ret
        path.pop()
        nbr.append(top)
      return []

    return dfs(["JFK"], graph, maxLen, "JFK")
