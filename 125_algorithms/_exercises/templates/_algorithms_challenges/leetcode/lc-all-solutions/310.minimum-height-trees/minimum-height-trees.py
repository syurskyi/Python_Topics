from collections ______ deque


class Solution(object
  ___ findMinHeightTrees(self, n, edges
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    __ le.(edges) __ 0:
      __ n > 0:
        r_ [0]
      r_   # list

    ___ bfs(graph, start
      queue = deque([(start, None)])
      level = 0
      maxLevel = -1
      farthest = None
      w___ queue:
        level += 1
        ___ i __ range(0, le.(queue)):
          label, parent = queue.popleft()
          ___ child __ graph.get(label,   # list
            __ child != parent:
              queue.append((child, label))
              __ level > maxLevel:
                maxLevel = level
                farthest = child
      r_ farthest

    ___ dfs(graph, start, end, visited, path, res
      __ start __ end:
        res.append(path +   # list)
        r_ True
      visited[start] = 1
      ___ child __ graph.get(start,   # list
        __ visited[child] __ 0:
          path.append(child)
          __ dfs(graph, child, end, visited, path, res
            r_ True
          path.p..

    graph = {}
    ___ edge __ edges:
      graph[edge[0]] = graph.get(edge[0],   # list) + [edge[1]]
      graph[edge[1]] = graph.get(edge[1],   # list) + [edge[0]]

    start = bfs(graph, edges[0][0])
    end = bfs(graph, start)
    res, visited =   # list, [0 ___ i __ range(0, n)]
    dfs(graph, start, end, visited, [start], res)
    __ not res:
      r_   # list
    path = res[0]
    __ le.(path) % 2 __ 0:
      r_ [path[le.(path) / 2 - 1], path[le.(path) / 2]]
    ____
      r_ [path[le.(path) / 2]]
