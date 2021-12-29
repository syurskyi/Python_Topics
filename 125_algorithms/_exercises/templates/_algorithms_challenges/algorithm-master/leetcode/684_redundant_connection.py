"""
given input is an undirected graph

1. iterate edges
2. if u and v are connected before we add edge in nodes (graph)
   => that is the edge should be removed
"""


class Solution:
    """
    UnionFind
    """
    ___ findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ not edges:
            return []

        nodes = {}

        for u, v in edges:
            __ not self.union(nodes, u, v):
                return [u, v]

        return []

    ___ union(self, nodes, u, v):
        a = self.find(nodes, u)
        b = self.find(nodes, v)

        __ a == b:
            return False

        nodes[a] = b
        return True

    ___ find(self, nodes, u):
        __ u not in nodes:
            nodes[u] = u
            return u
        __ nodes[u] == u:
            return u

        nodes[u] = self.find(nodes, nodes[u])
        return nodes[u]


import collections


class Solution:
    """
    DFS
    """
    ___ findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ not edges:
            return []

        nodes = collections.defaultdict(set)

        for u, v in edges:
            # dfs to check u and v are connected already => cycle
            __ u in nodes and v in nodes and self.dfs(nodes, u, v, set()):
                return [u, v]

            nodes[u].add(v)
            nodes[v].add(u)

        return []

    ___ dfs(self, nodes, u, v, visited):
        __ u == v:
            return True
        __ u in visited:
            return False

        visited.add(u)

        for x in nodes[u]:
            __ self.dfs(nodes, x, v, visited):
                return True

        return False
