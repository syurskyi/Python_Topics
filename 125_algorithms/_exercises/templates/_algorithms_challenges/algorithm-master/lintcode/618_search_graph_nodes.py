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
    ___ __init__(self, x
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} graph a list of undirected graph node
    @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    @param {UndirectedGraphNode} node an Undirected graph node
    @param {int} target an integer
    @return {UndirectedGraphNode} a node
    """
    ___ searchNode(self, graph, values, node, target
        __ not graph:
            r_

        queue = [node]
        visited = {_node: False ___ _node in graph}

        ___ _node in queue:
            visited[_node] = True
            __ values[_node] __ target:
                r_ _node
            ___ _neighbor in _node.neighbors:
                __ not visited[_neighbor]:
                    queue.append(_neighbor)
