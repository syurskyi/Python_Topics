____ collections _______ deque


class Solution(object):
  ___ findMinHeightTrees(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    __ l..(edges) __ 0:
      __ n > 0:
        r.. [0]
      r.. []

    ___ bfs(graph, start):
      queue = deque([(start, N..)])
      level = 0
      maxLevel = -1
      farthest = N..
      while queue:
        level += 1
        ___ i __ r..(0, l..(queue)):
          label, parent = queue.popleft()
          ___ child __ graph.get(label, []):
            __ child != parent:
              queue.a..((child, label))
              __ level > maxLevel:
                maxLevel = level
                farthest = child
      r.. farthest

    ___ dfs(graph, start, end, visited, path, res):
      __ start __ end:
        res.a..(path + [])
        r.. True
      visited[start] = 1
      ___ child __ graph.get(start, []):
        __ visited[child] __ 0:
          path.a..(child)
          __ dfs(graph, child, end, visited, path, res):
            r.. True
          path.pop()

    graph = {}
    ___ edge __ edges:
      graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
      graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]

    start = bfs(graph, edges[0][0])
    end = bfs(graph, start)
    res, visited    # list, [0 ___ i __ r..(0, n)]
    dfs(graph, start, end, visited, [start], res)
    __ n.. res:
      r.. []
    path = res[0]
    __ l..(path) % 2 __ 0:
      r.. [path[l..(path) / 2 - 1], path[l..(path) / 2]]
    ____:
      r.. [path[l..(path) / 2]]
