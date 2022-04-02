"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


c_ Solution:
    """
    Union Find
    """
    ___ connectedSet  nodes
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        __ n.. nodes:
            r.. []

        uf    # dict

        ___ node __ nodes:
            ___ neib __ node.neighbors:
                union(uf, node, neib)

        ans    # dict

        ___ node __ nodes:
            # to correct root again
            root = find(uf, node)

            __ root n.. __ ans:
                ans[root]    # list

            ans[root].a..(node.label)

        r.. l..(ans.values())

    ___ union  nodes, a, b
        _a = find(nodes, a)
        _b = find(nodes, b)

        __ _a __ n.. _b:
            nodes[_b] = _a

    ___ find  nodes, a
        __ a n.. __ nodes:
            nodes[a] = a
            r.. a
        __ nodes[a] __ a:
            r.. a

        nodes[a] = find(nodes, nodes[a])
        r.. nodes[a]


c_ Solution:
    """
    DFS
    """
    ___ connectedSet  nodes
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        ans    # list

        __ n.. nodes:
            r.. ans

        visited = s..()

        ___ node __ nodes:
            __ node __ visited:
                _____

            path    # list
            dfs(node, visited, path)
            ans.a..(s..(path))

        r.. ans

    ___ dfs  a, visited, path
        visited.add(a)
        path.a..(a.label)

        ___ b __ a.neighbors:
            __ b __ visited:
                _____

            dfs(b, visited, path)
