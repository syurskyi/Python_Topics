"""
Definition for a directed graph node
class DirectedGraphNode:
    ___ __init__(self, x
        self.label = x
        self.neighbors = []
"""


class Solution:
    ___ __init__(self
        self.nodes = {}

    """
    @param {DirectedGraphNode[]} nodes a array of directed graph node
    @return {int[][]} a connected set of a directed graph
    """
    ___ connectedSet2(self, nodes
        # Build UnionFind
        ___ node in nodes:
            ___ nei in node.neighbors:
                self.connect(nei.label, node.label)

        # Categorify result
        result = {}
        root_label = ''
        ___ node in nodes:
            root_label = self.find(node.label)
            __ root_label not in result:
                result[root_label] = []
            result[root_label].append(node.label)
        r_ result.values()

    ___ connect(self, a, b
        root_a = self.find(a)
        root_b = self.find(b)
        __ root_a is not root_b:
            self.nodes[root_a] = root_b

    ___ find(self, a
        __ a not in self.nodes:
            self.nodes[a] = a
            r_ a
        ____ self.nodes[a] is a:
            r_ a
        self.nodes[a] = self.find(self.nodes[a])
        r_ self.nodes[a]
