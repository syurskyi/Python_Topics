c_ Solution(object):
  ___ findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    ___ dfs(start, visited, graph, ans):
      visited[start] = 1
      ___ nbr __ graph[start]:
        __ visited[nbr] __ 1:
          r.. F..
        __ visited[nbr] != 0:
          continue
        __ dfs(nbr, visited, graph, ans) __ F..:
          r.. F..
      ans.a..(start)
      visited[start] = 2
      r.. T..

    graph = [[] ___ _ __ r..(0, numCourses)]
    ans    # list

    ___ pre __ prerequisites:
      start, end = pre
      graph[start].a..(end)

    visited = [0 ___ _ __ r..(0, numCourses)]

    ___ pre __ prerequisites:
      start, end = pre
      __ visited[start] != 0:
        continue
      __ dfs(start, visited, graph, ans) __ F..:
        r.. []
    ___ i __ r..(0, numCourses):
      __ visited[i] __ 0:
        ans.a..(i)
    r.. ans
