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

        BFS
        """
        __ node is None:
            r_ None
        queue = []
        start_cloned_node = UndirectedGraphNode(node.label)
        visited = set()
        # A dictionary that maps labels to cloned nodes
        d = {node: start_cloned_node}
        queue.append(node)
        w___ queue:
            node = queue.pop(0)
            visited.add(node)
            cloned_node = d[node]
            cloned_neighbors = []
            for neighbor in node.neighbors:
                __ neighbor not in visited:
                    queue.append(neighbor)
                __ neighbor not in d:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = cloned_neighbor
                ____
                    cloned_neighbor = d[neighbor]
                cloned_neighbors.append(cloned_neighbor)
            cloned_node.neighbors = cloned_neighbors
        r_ start_cloned_node
