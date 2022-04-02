"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


"""
Iteration
"""
c_ Solution:
    ___ cloneGraph  node
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        __ n.. node:
            r..

        queue = [node]
        root = UndirectedGraphNode(node.label)
        N = {root.label: root}

        ___ node __ queue:
            ___ neighbor __ node.neighbors:
                _node = N..
                __ neighbor.label __ N:
                    _node = N[neighbor.label]
                ____:
                    _node = UndirectedGraphNode(neighbor.label)
                    N[neighbor.label] = _node
                    queue.a..(neighbor)

                N[node.label].neighbors.a..(_node)

        r.. root


"""
Recursion
"""
c_ Solution:
    ___ cloneGraph  node
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        __ n.. node:
            r..

        r.. dfs(node, {})

    ___ dfs  node, N
        __ node.label __ N:
            r.. N[node.label]

        N[node.label] = UndirectedGraphNode(node.label)
        ___ neighbor __ node.neighbors:
            N[node.label].neighbors.a..(dfs(neighbor, N))

        r.. N[node.label]
