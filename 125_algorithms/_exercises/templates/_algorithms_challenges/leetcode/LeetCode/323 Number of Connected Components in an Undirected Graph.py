"""
Premium Question
simple DFS
"""
__author__ = 'Daniel'


class Solution(object
    ___ countComponents(self, n, edges
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        V = [[] ___ _ in xrange(n)]
        ___ e in edges:
            V[e[0]].append(e[1])
            V[e[1]].append(e[0])

        visited = [False ___ _ in xrange(n)]
        cnt = 0
        ___ v in xrange(n
            __ not visited[v]:
                cnt += 1
                self.dfs(V, v, visited)

        r_ cnt

    ___ dfs(self, V, v, visited
        visited[v] = True
        ___ nbr in V[v]:
            __ not visited[nbr]:
                self.dfs(V, nbr, visited)
