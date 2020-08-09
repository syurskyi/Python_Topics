"""
Definition for a Directed graph node
class DirectedGraphNode:
    ___ __init__(self, x
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    ___ topSort(self, graph
        ans = []
        __ not graph:
            r_ ans

        indegs = {}
        ___ node in graph:
            __ node not in indegs:
                indegs[node] = 0
            ___ _node in node.neighbors:
                __ _node not in indegs:
                    indegs[_node] = 0
                indegs[_node] += 1

        queue = [node ___ node, indeg in indegs.items() __ indeg __ 0]
        ___ node in queue:
            ans.append(node)
            ___ _node in node.neighbors:
                indegs[_node] -= 1
                __ indegs[_node] __ 0:
                    queue.append(_node)

        r_ ans
