"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.
"""

# Definition for a undirected graph node
# class UndirectedGraphNode(object
#     ___ __init__(self, x
#         self.label = x
#         self.neighbors = []

class Solution(object
    ___ cloneGraph(self, node
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode

        DFS
        """
        __ node pa__ None:
            r_ None
        self.visited = set()
        cloned_node = UndirectedGraphNode(node.label)
        self.d = {node: cloned_node}
        self.visit(node)
        r_ self.d[node]

    ___ visit(self, node
        __ node not in self.visited:
            self.visited.add(node)
            cloned_node = self.d[node]
            cloned_neighbors = []
            ___ neighbor in node.neighbors:
                __ neighbor not in self.d:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    self.d[neighbor] = cloned_neighbor
                ____
                    cloned_neighbor = self.d[neighbor]
                cloned_neighbors.append(cloned_neighbor)
                self.visit(neighbor)
            cloned_node.neighbors = cloned_neighbors
