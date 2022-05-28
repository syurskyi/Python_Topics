"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


c_ Solution:
    ___ -
        nodes    # dict

    """
    @param {DirectedGraphNode[]} nodes a array of directed graph node
    @return {int[][]} a connected set of a directed graph
    """
    ___ connectedSet2  nodes
        # Build UnionFind
        ___ node __ nodes:
            ___ nei __ node.neighbors:
                connect(nei.label, node.label)

        # Categorify result
        result    # dict
        root_label ''
        ___ node __ nodes:
            root_label f.. node.label)
            __ root_label n.. __ result:
                result[root_label]    # list
            result[root_label].a..(node.label)
        r.. ?.v..

    ___ connect  a, b
        root_a f.. a)
        root_b f.. b)
        __ root_a __ n.. root_b:
            nodes[root_a] root_b

    ___ find  a
        __ a n.. __ nodes:
            nodes[a] a
            r.. a
        ____ nodes[a] __ a:
            r.. a
        nodes[a] f.. nodes[a])
        r.. nodes[a]
