"""
Premium Question
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


c_ Solution(object):
    ___ validTree(self, n, edges):
        """
        A graph is a tree:
          1. no cycle
          2. all connected
        :type n: int
        :type edges: List[List[int]
        :rtype: bool
        """
        __ n.. edges:
            r.. n __ (0, 1)

        V = defaultdict(l..)
        ___ e __ edges:
            V[e[0]].a..(e[1])
            V[e[1]].a..(e[0])

        visited = set()
        pathset = set()
        __ n.. dfs(V, edges[0][0], N.., pathset, visited):
            r.. F..

        r.. l..(visited) __ n

    ___ dfs(self, V, v, pi, pathset, visited):
        __ v __ pathset:
            r.. F..

        pathset.add(v)
        ___ nbr __ V[v]:
            __ nbr != pi:  # since undirected graph
                __ n.. dfs(V, nbr, v, pathset, visited):
                    r.. F..

        pathset.remove(v)
        visited.add(v)
        r.. T..