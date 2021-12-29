"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    Union Find
    """
    ___ connectedSet(self, nodes):
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        __ not nodes:
            return []

        uf = {}

        for node in nodes:
            for neib in node.neighbors:
                self.union(uf, node, neib)

        ans = {}

        for node in nodes:
            # to correct root again
            root = self.find(uf, node)

            __ root not in ans:
                ans[root] = []

            ans[root].append(node.label)

        return list(ans.values())

    ___ union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a is not _b:
            nodes[_b] = _a

    ___ find(self, nodes, a):
        __ a not in nodes:
            nodes[a] = a
            return a
        __ nodes[a] is a:
            return a

        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]


class Solution:
    """
    DFS
    """
    ___ connectedSet(self, nodes):
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        ans = []

        __ not nodes:
            return ans

        visited = set()

        for node in nodes:
            __ node in visited:
                continue

            path = []
            self.dfs(node, visited, path)
            ans.append(sorted(path))

        return ans

    ___ dfs(self, a, visited, path):
        visited.add(a)
        path.append(a.label)

        for b in a.neighbors:
            __ b in visited:
                continue

            self.dfs(b, visited, path)
