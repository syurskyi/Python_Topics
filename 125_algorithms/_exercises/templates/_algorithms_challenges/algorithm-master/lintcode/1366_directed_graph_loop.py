_______ c..


c_ Solution:
    """
    @param start: The start points set
    @param end: The end points set
    @return: Return if the graph is cyclic
    """
    ___ isCyclicGraph  start, end):
        __ n.. start o. n.. end o. l..(start) != l..(end):
            r.. F..

        n = l..(start)
        nxt = c...defaultdict(s..)
        visited = s..()
        rec_stack = s..()

        ___ i __ r..(n):
            nxt[start[i]].add(end[i])

        ___ i __ r..(n):
            __ start[i] __ visited:
                _____
            __ dfs(start[i], nxt, visited, rec_stack):
                r.. T..

        r.. F..

    ___ dfs  u, nxt, visited, rec_stack):
        __ u n.. __ nxt:
            r.. F..

        visited.add(u)
        rec_stack.add(u)

        ___ v __ nxt[u]:
            __ v __ rec_stack:
                r.. T..

            __ v n.. __ visited a.. dfs(v, nxt, visited, rec_stack):
                r.. T..

        rec_stack.discard(u)
        r.. F..
