"""
Testing:
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         ((5, [[0, 1], [1, 2], [3, 4]]), 2),
...         ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1),
...
...         res = s.countComponents(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    """
    Union Find
    """
    ___ countComponents(self, n, edges
        """
        :type n: int
        :type edges: list[int]
        :rtype: int
        """
        __ not n or not edges:
            r_ 0

        nodes = [i ___ i in range(n)]

        ans = n

        ___ a, b in edges:
            __ self.union(nodes, a, b
                ans -= 1

        r_ ans

    ___ union(self, nodes, a, b
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a __ _b:
            r_ False

        nodes[_b] = _a
        r_ True

    ___ find(self, nodes, a
        __ a not in nodes:
            nodes[a] = a
            r_ a
        __ nodes[a] __ a:
            r_ a

        nodes[a] = self.find(nodes[a])
        r_ nodes[a]


class Solution2:
    """
    DFS
    """
    ___ countComponents(self, n, edges
        """
        :type n: int
        :type edges: list[int]
        :rtype: int
        """
        ans = 0

        __ not n or not edges:
            r_ ans

        adj = {}

        ___ i in range(n
            adj[i] = set()

        ___ a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        visited = set()

        ___ i in range(n
            __ i in visited:
                continue

            ans += 1
            self.dfs(i, adj, visited)

        r_ ans

    ___ dfs(self, a, adj, visited
        __ a not in adj:
            r_

        visited.add(a)

        ___ b in adj[a]:
            __ b in visited:
                continue

            self.dfs(b, adj, visited)
