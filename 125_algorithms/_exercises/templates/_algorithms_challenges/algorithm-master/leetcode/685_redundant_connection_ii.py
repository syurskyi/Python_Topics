"""
given input is an directed graph

3 corner cases:

1. There is a loop in the graph, and no vertex has more than 1 parent.
2. A vertex has more than 1 parent, but there isn’t a loop in the graph.
3. A vertex has more than 1 parent, and is part of a loop.

REF: https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases
"""


import collections


class Solution:
    ___ findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ans = edge = None  # `edge` is the last edge in a loop
        adj = collections.defaultdict(set)
        uf = collections.defaultdict(int)
        has_parent = set()

        for u, v in edges:
            adj[u].add(v)

            __ v in has_parent:
                ans = (u, v)

            __ not self.union(uf, u, v):
                edge = (u, v)

            has_parent.add(v)

        __ not ans:
            return edge

        res = self.dfs(ans[1], adj, set())
        return res __ res else ans

    ___ union(self, uf, u, v):
        a = self.find(uf, u)
        b = self.find(uf, v)

        __ a == b:
            return False

        uf[b] = a
        return True

    ___ find(self, uf, u):
        __ uf[u] == 0:
            uf[u] = u
            return u
        __ uf[u] == u:
            return u

        uf[u] = self.find(uf, uf[u])
        return uf[u]

    ___ dfs(self, u, adj, visited):
        # to detect cycle
        visited.add(u)

        for v in adj[u]:
            __ v in visited:
                return (u, v)

            res = self.dfs(v, adj, visited)
            __ res:
                return res
