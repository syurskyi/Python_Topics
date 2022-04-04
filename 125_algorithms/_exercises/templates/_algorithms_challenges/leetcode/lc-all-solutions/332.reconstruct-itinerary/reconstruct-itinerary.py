____ c.. _______ d..


c_ Solution(o..
  ___ findItinerary  tickets
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph    # dict
    hashset = s..([])
    ___ ticket __ tickets:
      graph[ticket[0]] = graph.g.. ticket[0], []) + [ticket[1]]

    maxLen = l..(tickets) + 1

    ___ k __ graph:
      graph[k] = d..(s..(graph[k]

    ___ dfs(p.., graph, maxLen, start
      __ l..(p..) __ maxLen:
        r.. p.. + []
      ___ k __ r..(0, l..(graph.g.. start, []))):
        nbr = graph.g.. start, [])
        top = nbr.popleft()
        p...a..(top)
        ret = dfs(p.., graph, maxLen, top)
        __ ret:
          r.. ret
        p...p.. )
        nbr.a..(top)
      r.. []

    r.. dfs(["JFK"], graph, maxLen, "JFK")
