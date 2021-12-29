class Solution(object):
  ___ canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    ___ dfs(start, parent, visited, graph):
      visited[start] = 1
      for nbr in graph[start]:
        __ visited[nbr] == 1:
          return False
        __ dfs(nbr, start, visited, graph) == False:
          return False
      visited[start] = 2
      return True

    graph = [[] for _ in range(0, numCourses)]
    for pre in prerequisites:
      start, end = pre
      graph[start].append(end)

    visited = [0 for _ in range(0, numCourses)]

    for pre in prerequisites:
      start, end = pre
      __ visited[start] == 0:
        __ dfs(start, None, visited, graph) == False:
          return False
    return True
