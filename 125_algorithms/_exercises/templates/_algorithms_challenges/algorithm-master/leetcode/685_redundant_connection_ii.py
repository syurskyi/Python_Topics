"""
given input is an directed graph

3 corner cases:

1. There is a loop in the graph, and no vertex has more than 1 parent.
2. A vertex has more than 1 parent, but there isn’t a loop in the graph.
3. A vertex has more than 1 parent, and is part of a loop.

REF: https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases
"""


_______ c..


c_ Solution:
    ___ findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ans = edge = N..  # `edge` is the last edge in a loop
        adj = c...defaultdict(set)
        uf = c...defaultdict(i..)
        has_parent = set()

        ___ u, v __ edges:
            adj[u].add(v)

            __ v __ has_parent:
                ans = (u, v)

            __ n.. union(uf, u, v):
                edge = (u, v)

            has_parent.add(v)

        __ n.. ans:
            r.. edge

        res = dfs(ans[1], adj, set())
        r.. res __ res ____ ans

    ___ union(self, uf, u, v):
        a = find(uf, u)
        b = find(uf, v)

        __ a __ b:
            r.. F..

        uf[b] = a
        r.. T..

    ___ find(self, uf, u):
        __ uf[u] __ 0:
            uf[u] = u
            r.. u
        __ uf[u] __ u:
            r.. u

        uf[u] = find(uf, uf[u])
        r.. uf[u]

    ___ dfs(self, u, adj, visited):
        # to detect cycle
        visited.add(u)

        ___ v __ adj[u]:
            __ v __ visited:
                r.. (u, v)

            res = dfs(v, adj, visited)
            __ res:
                r.. res
