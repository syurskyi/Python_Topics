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
        __ n.. nodes:
            r.. []

        uf = {}

        ___ node __ nodes:
            ___ neib __ node.neighbors:
                self.union(uf, node, neib)

        ans = {}

        ___ node __ nodes:
            # to correct root again
            root = self.find(uf, node)

            __ root n.. __ ans:
                ans[root]    # list

            ans[root].a..(node.label)

        r.. l..(ans.values())

    ___ union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a __ n.. _b:
            nodes[_b] = _a

    ___ find(self, nodes, a):
        __ a n.. __ nodes:
            nodes[a] = a
            r.. a
        __ nodes[a] __ a:
            r.. a

        nodes[a] = self.find(nodes, nodes[a])
        r.. nodes[a]


class Solution:
    """
    DFS
    """
    ___ connectedSet(self, nodes):
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        ans    # list

        __ n.. nodes:
            r.. ans

        visited = set()

        ___ node __ nodes:
            __ node __ visited:
                continue

            path    # list
            self.dfs(node, visited, path)
            ans.a..(s..(path))

        r.. ans

    ___ dfs(self, a, visited, path):
        visited.add(a)
        path.a..(a.label)

        ___ b __ a.neighbors:
            __ b __ visited:
                continue

            self.dfs(b, visited, path)
