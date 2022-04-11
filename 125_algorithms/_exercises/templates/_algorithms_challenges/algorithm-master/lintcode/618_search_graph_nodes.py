"""
Test Case:

{1}
[0]
1
0
"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


c_ Solution:
    """
    @param {UndirectedGraphNode[]} graph a list of undirected graph node
    @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    @param {UndirectedGraphNode} node an Undirected graph node
    @param {int} target an integer
    @return {UndirectedGraphNode} a node
    """
    ___ searchNode  graph, values, node, target
        __ n.. graph:
            r..

        queue [node]
        visited {_node: F.. ___ _node __ graph}

        ___ _node __ queue:
            visited[_node] T..
            __ values[_node] __ target:
                r.. _node
            ___ _neighbor __ _node.neighbors:
                __ n.. visited[_neighbor]:
                    queue.a..(_neighbor)
