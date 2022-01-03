"""
Premium Question
simple DFS
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        V = [[] ___ _ __ xrange(n)]
        ___ e __ edges:
            V[e[0]].a..(e[1])
            V[e[1]].a..(e[0])

        visited = [F.. ___ _ __ xrange(n)]
        cnt = 0
        ___ v __ xrange(n):
            __ n.. visited[v]:
                cnt += 1
                dfs(V, v, visited)

        r.. cnt

    ___ dfs(self, V, v, visited):
        visited[v] = T..
        ___ nbr __ V[v]:
            __ n.. visited[nbr]:
                dfs(V, nbr, visited)
