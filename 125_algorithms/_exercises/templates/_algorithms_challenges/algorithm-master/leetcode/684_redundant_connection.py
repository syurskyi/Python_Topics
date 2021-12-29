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
        __ n.. edges:
            r.. []

        nodes = {}

        ___ u, v __ edges:
            __ n.. self.union(nodes, u, v):
                r.. [u, v]

        r.. []

    ___ union(self, nodes, u, v):
        a = self.find(nodes, u)
        b = self.find(nodes, v)

        __ a __ b:
            r.. False

        nodes[a] = b
        r.. True

    ___ find(self, nodes, u):
        __ u n.. __ nodes:
            nodes[u] = u
            r.. u
        __ nodes[u] __ u:
            r.. u

        nodes[u] = self.find(nodes, nodes[u])
        r.. nodes[u]


_______ collections


class Solution:
    """
    DFS
    """
    ___ findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n.. edges:
            r.. []

        nodes = collections.defaultdict(set)

        ___ u, v __ edges:
            # dfs to check u and v are connected already => cycle
            __ u __ nodes and v __ nodes and self.dfs(nodes, u, v, set()):
                r.. [u, v]

            nodes[u].add(v)
            nodes[v].add(u)

        r.. []

    ___ dfs(self, nodes, u, v, visited):
        __ u __ v:
            r.. True
        __ u __ visited:
            r.. False

        visited.add(u)

        ___ x __ nodes[u]:
            __ self.dfs(nodes, x, v, visited):
                r.. True

        r.. False
