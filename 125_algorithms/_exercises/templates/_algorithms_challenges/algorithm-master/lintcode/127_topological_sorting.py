"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


c_ Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    ___ topSort  graph
        ans    # list
        __ n.. graph:
            r.. ans

        indegs    # dict
        ___ node __ graph:
            __ node n.. __ indegs:
                indegs[node] = 0
            ___ _node __ node.neighbors:
                __ _node n.. __ indegs:
                    indegs[_node] = 0
                indegs[_node] += 1

        queue = [node ___ node, indeg __ indegs.i.. __ indeg __ 0]
        ___ node __ queue:
            ans.a..(node)
            ___ _node __ node.neighbors:
                indegs[_node] -= 1
                __ indegs[_node] __ 0:
                    queue.a..(_node)

        r.. ans
