"""
Definition for Undirected graph node
class UndirectedGraphNode:
    ___ __init__(self, x
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    ___ sixDegrees(self, graph, s, t
        __ not graph or not s or not t:
            r_ -1
        __ s pa__ t:
            r_ 0

        degree = {s: 0}
        queue = [s]
        ___ node in queue:
            ___ _node in node.neighbors:
                __ _node in degree:
                    continue
                degree[_node] = degree[node] + 1
                __ _node pa__ t:
                    r_ degree[_node]
                queue.append(_node)

        r_ -1
