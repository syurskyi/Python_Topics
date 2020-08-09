class Solution(object
  ___ findOrder(self, numCourses, prerequisites
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    ___ dfs(start, visited, graph, ans
      visited[start] = 1
      for nbr in graph[start]:
        __ visited[nbr] __ 1:
          r_ False
        __ visited[nbr] != 0:
          continue
        __ dfs(nbr, visited, graph, ans) __ False:
          r_ False
      ans.append(start)
      visited[start] = 2
      r_ True

    graph = [[] for _ in range(0, numCourses)]
    ans = []

    for pre in prerequisites:
      start, end = pre
      graph[start].append(end)

    visited = [0 for _ in range(0, numCourses)]

    for pre in prerequisites:
      start, end = pre
      __ visited[start] != 0:
        continue
      __ dfs(start, visited, graph, ans) __ False:
        r_ []
    for i in range(0, numCourses
      __ visited[i] __ 0:
        ans.append(i)
    r_ ans
