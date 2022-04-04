"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.
"""

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

c_ Solution(o..
    ___ cloneGraph  node
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode

        BFS
        """
        __ node __ N..
            r.. N..
        queue    # list
        start_cloned_node = UndirectedGraphNode(node.label)
        visited = s..()
        # A dictionary that maps labels to cloned nodes
        d = {node: start_cloned_node}
        queue.a..(node)
        w.... queue:
            node = queue.p.. 0)
            visited.add(node)
            cloned_node = d[node]
            cloned_neighbors    # list
            ___ neighbor __ node.neighbors:
                __ neighbor n.. __ visited:
                    queue.a..(neighbor)
                __ neighbor n.. __ d:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = cloned_neighbor
                ____
                    cloned_neighbor = d[neighbor]
                cloned_neighbors.a..(cloned_neighbor)
            cloned_node.neighbors = cloned_neighbors
        r.. start_cloned_node
