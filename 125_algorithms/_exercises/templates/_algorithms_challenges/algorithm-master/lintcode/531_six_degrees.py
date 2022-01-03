"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


c_ Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    ___ sixDegrees(self, graph, s, t):
        __ n.. graph o. n.. s o. n.. t:
            r.. -1
        __ s __ t:
            r.. 0

        degree = {s: 0}
        queue = [s]
        ___ node __ queue:
            ___ _node __ node.neighbors:
                __ _node __ degree:
                    continue
                degree[_node] = degree[node] + 1
                __ _node __ t:
                    r.. degree[_node]
                queue.a..(_node)

        r.. -1
