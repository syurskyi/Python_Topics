c_ Solution:
    ___ isBipartite  graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color    # dict

        ___ node __ r..(l..(graph)):
            __ node n.. __ color:
                color[node] = 0
            ___ nei __ graph[node]:
                __ nei n.. __ color:
                    color[nei] = color[node] ^ 1
                ____ color[nei] __ color[node]:
                    r.. F..

        r.. T..
