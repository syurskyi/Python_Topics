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
    ___ findRedundantConnection(self, edges
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ not edges:
            r_ []

        nodes = {}

        ___ u, v in edges:
            __ not self.union(nodes, u, v
                r_ [u, v]

        r_ []

    ___ union(self, nodes, u, v
        a = self.find(nodes, u)
        b = self.find(nodes, v)

        __ a __ b:
            r_ False

        nodes[a] = b
        r_ True

    ___ find(self, nodes, u
        __ u not in nodes:
            nodes[u] = u
            r_ u
        __ nodes[u] __ u:
            r_ u

        nodes[u] = self.find(nodes, nodes[u])
        r_ nodes[u]


______ collections


class Solution:
    """
    DFS
    """
    ___ findRedundantConnection(self, edges
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ not edges:
            r_ []

        nodes = collections.defaultdict(set)

        ___ u, v in edges:
            # dfs to check u and v are connected already => cycle
            __ u in nodes and v in nodes and self.dfs(nodes, u, v, set()):
                r_ [u, v]

            nodes[u].add(v)
            nodes[v].add(u)

        r_ []

    ___ dfs(self, nodes, u, v, visited
        __ u __ v:
            r_ True
        __ u in visited:
            r_ False

        visited.add(u)

        ___ x in nodes[u]:
            __ self.dfs(nodes, x, v, visited
                r_ True

        r_ False
