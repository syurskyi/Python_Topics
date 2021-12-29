"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    ___ __init__(self):
        self.nodes = {}

    """
    @param {DirectedGraphNode[]} nodes a array of directed graph node
    @return {int[][]} a connected set of a directed graph
    """
    ___ connectedSet2(self, nodes):
        # Build UnionFind
        ___ node __ nodes:
            ___ nei __ node.neighbors:
                self.connect(nei.label, node.label)

        # Categorify result
        result = {}
        root_label = ''
        ___ node __ nodes:
            root_label = self.find(node.label)
            __ root_label n.. __ result:
                result[root_label]    # list
            result[root_label].a..(node.label)
        r.. result.values()

    ___ connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        __ root_a __ n.. root_b:
            self.nodes[root_a] = root_b

    ___ find(self, a):
        __ a n.. __ self.nodes:
            self.nodes[a] = a
            r.. a
        ____ self.nodes[a] __ a:
            r.. a
        self.nodes[a] = self.find(self.nodes[a])
        r.. self.nodes[a]
