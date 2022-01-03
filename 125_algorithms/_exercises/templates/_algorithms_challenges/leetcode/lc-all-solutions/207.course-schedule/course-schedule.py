c_ Solution(object):
  ___ canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    ___ dfs(start, parent, visited, graph):
      visited[start] = 1
      ___ nbr __ graph[start]:
        __ visited[nbr] __ 1:
          r.. F..
        __ dfs(nbr, start, visited, graph) __ F..:
          r.. F..
      visited[start] = 2
      r.. T..

    graph = [[] ___ _ __ r..(0, numCourses)]
    ___ pre __ prerequisites:
      start, end = pre
      graph[start].a..(end)

    visited = [0 ___ _ __ r..(0, numCourses)]

    ___ pre __ prerequisites:
      start, end = pre
      __ visited[start] __ 0:
        __ dfs(start, N.., visited, graph) __ F..:
          r.. F..
    r.. T..
