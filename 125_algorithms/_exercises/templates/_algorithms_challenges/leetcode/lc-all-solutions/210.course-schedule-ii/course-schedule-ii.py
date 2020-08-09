class Solution(object
  ___ findOrder(self, numCourses, prerequisites
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    ___ dfs(start, visited, graph, ans
      visited[start] = 1
      ___ nbr in graph[start]:
        __ visited[nbr] __ 1:
          r_ False
        __ visited[nbr] != 0:
          continue
        __ dfs(nbr, visited, graph, ans) __ False:
          r_ False
      ans.append(start)
      visited[start] = 2
      r_ True

    graph = [[] ___ _ in range(0, numCourses)]
    ans = []

    ___ pre in prerequisites:
      start, end = pre
      graph[start].append(end)

    visited = [0 ___ _ in range(0, numCourses)]

    ___ pre in prerequisites:
      start, end = pre
      __ visited[start] != 0:
        continue
      __ dfs(start, visited, graph, ans) __ False:
        r_ []
    ___ i in range(0, numCourses
      __ visited[i] __ 0:
        ans.append(i)
    r_ ans
