"""
Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    ___ validTree(self, n, edges):
        """
        A graph is a tree:
          1. no cycle
          2. all connected
        :type n: int
        :type edges: List[List[int]
        :rtype: bool
        """
        __ not edges:
            return n in (0, 1)

        V = defaultdict(list)
        for e in edges:
            V[e[0]].append(e[1])
            V[e[1]].append(e[0])

        visited = set()
        pathset = set()
        __ not self.dfs(V, edges[0][0], None, pathset, visited):
            return False

        return len(visited) == n

    ___ dfs(self, V, v, pi, pathset, visited):
        __ v in pathset:
            return False

        pathset.add(v)
        for nbr in V[v]:
            __ nbr != pi:  # since undirected graph
                __ not self.dfs(V, nbr, v, pathset, visited):
                    return False

        pathset.remove(v)
        visited.add(v)
        return True