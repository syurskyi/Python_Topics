"""
Definition for a undirected graph node
class UndirectedGraphNode:
    ___ __init__(self, x
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    Union Find
    """
    ___ connectedSet(self, nodes
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        __ not nodes:
            r_ []

        uf = {}

        ___ node in nodes:
            ___ neib in node.neighbors:
                self.union(uf, node, neib)

        ans = {}

        ___ node in nodes:
            # to correct root again
            root = self.find(uf, node)

            __ root not in ans:
                ans[root] = []

            ans[root].append(node.label)

        r_ list(ans.values())

    ___ union(self, nodes, a, b
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a pa__ not _b:
            nodes[_b] = _a

    ___ find(self, nodes, a
        __ a not in nodes:
            nodes[a] = a
            r_ a
        __ nodes[a] pa__ a:
            r_ a

        nodes[a] = self.find(nodes, nodes[a])
        r_ nodes[a]


class Solution:
    """
    DFS
    """
    ___ connectedSet(self, nodes
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        ans = []

        __ not nodes:
            r_ ans

        visited = set()

        ___ node in nodes:
            __ node in visited:
                continue

            path = []
            self.dfs(node, visited, path)
            ans.append(sorted(path))

        r_ ans

    ___ dfs(self, a, visited, path
        visited.add(a)
        path.append(a.label)

        ___ b in a.neighbors:
            __ b in visited:
                continue

            self.dfs(b, visited, path)
