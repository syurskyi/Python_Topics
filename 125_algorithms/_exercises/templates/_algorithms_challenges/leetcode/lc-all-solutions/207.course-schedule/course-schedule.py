class Solution(object
  ___ canFinish(self, numCourses, prerequisites
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    ___ dfs(start, parent, visited, graph
      visited[start] = 1
      ___ nbr __ graph[start]:
        __ visited[nbr] __ 1:
          r_ False
        __ dfs(nbr, start, visited, graph) __ False:
          r_ False
      visited[start] = 2
      r_ True

    graph = [[] ___ _ __ range(0, numCourses)]
    ___ pre __ prerequisites:
      start, end = pre
      graph[start].append(end)

    visited = [0 ___ _ __ range(0, numCourses)]

    ___ pre __ prerequisites:
      start, end = pre
      __ visited[start] __ 0:
        __ dfs(start, None, visited, graph) __ False:
          r_ False
    r_ True
