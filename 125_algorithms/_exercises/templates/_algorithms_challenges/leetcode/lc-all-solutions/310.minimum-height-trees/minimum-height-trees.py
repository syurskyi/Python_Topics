____ c.. _______ d..


c_ Solution(o..
  ___ findMinHeightTrees  n, edges
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    __ l..(edges) __ 0:
      __ n > 0:
        r.. [0]
      r.. []

    ___ bfs(graph, start
      queue d..([(start, N..)])
      level 0
      maxLevel -1
      farthest N..
      w.... queue:
        level += 1
        ___ i __ r..(0, l..(queue:
          label, parent queue.popleft()
          ___ child __ graph.g.. label, []
            __ child !_ parent:
              queue.a..((child, label
              __ level > maxLevel:
                maxLevel level
                farthest child
      r.. farthest

    ___ dfs(graph, start, end, visited, p.., res
      __ start __ end:
        res.a..(p.. + [])
        r.. T..
      visited[start] 1
      ___ child __ graph.g.. start, []
        __ visited[child] __ 0:
          p...a..(child)
          __ dfs(graph, child, end, visited, p.., res
            r.. T..
          p...p.. )

    graph    # dict
    ___ edge __ edges:
      graph[edge[0]] graph.g.. edge[0], []) + [edge[1]]
      graph[edge[1]] graph.g.. edge[1], []) + [edge[0]]

    start bfs(graph, edges[0][0])
    end bfs(graph, start)
    res, visited    # list, [0 ___ i __ r..(0, n)]
    dfs(graph, start, end, visited, [start], res)
    __ n.. res:
      r.. []
    p.. res[0]
    __ l..(p..) % 2 __ 0:
      r.. [p..[l..(p..) / 2 - 1], p..[l..(p..) / 2]]
    ____
      r.. [p..[l..(p..) / 2]]
