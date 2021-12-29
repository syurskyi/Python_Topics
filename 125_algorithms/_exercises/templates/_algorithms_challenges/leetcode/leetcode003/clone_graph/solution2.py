"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.
"""

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    ___ cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode

        DFS
        """
        __ node __ N..
            r.. N..
        self.visited = set()
        cloned_node = UndirectedGraphNode(node.label)
        self.d = {node: cloned_node}
        self.visit(node)
        r.. self.d[node]

    ___ visit(self, node):
        __ node n.. __ self.visited:
            self.visited.add(node)
            cloned_node = self.d[node]
            cloned_neighbors    # list
            ___ neighbor __ node.neighbors:
                __ neighbor n.. __ self.d:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    self.d[neighbor] = cloned_neighbor
                ____:
                    cloned_neighbor = self.d[neighbor]
                cloned_neighbors.a..(cloned_neighbor)
                self.visit(neighbor)
            cloned_node.neighbors = cloned_neighbors
