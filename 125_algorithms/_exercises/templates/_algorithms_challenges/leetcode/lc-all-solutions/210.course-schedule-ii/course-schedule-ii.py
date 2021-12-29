class Solution(object):
  ___ findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    ___ dfs(start, visited, graph, ans):
      visited[start] = 1
      for nbr in graph[start]:
        __ visited[nbr] == 1:
          return False
        __ visited[nbr] != 0:
          continue
        __ dfs(nbr, visited, graph, ans) == False:
          return False
      ans.append(start)
      visited[start] = 2
      return True

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
      __ dfs(start, visited, graph, ans) == False:
        return []
    for i in range(0, numCourses):
      __ visited[i] == 0:
        ans.append(i)
    return ans
