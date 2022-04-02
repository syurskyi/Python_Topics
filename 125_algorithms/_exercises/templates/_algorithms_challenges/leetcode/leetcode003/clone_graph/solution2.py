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

        DFS
        """
        __ node __ N..
            r.. N..
        visited = s..()
        cloned_node = UndirectedGraphNode(node.label)
        d = {node: cloned_node}
        visit(node)
        r.. d[node]

    ___ visit  node
        __ node n.. __ visited:
            visited.add(node)
            cloned_node = d[node]
            cloned_neighbors    # list
            ___ neighbor __ node.neighbors:
                __ neighbor n.. __ d:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = cloned_neighbor
                ____:
                    cloned_neighbor = d[neighbor]
                cloned_neighbors.a..(cloned_neighbor)
                visit(neighbor)
            cloned_node.neighbors = cloned_neighbors
