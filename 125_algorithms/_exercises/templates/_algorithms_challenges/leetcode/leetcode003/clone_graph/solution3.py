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
        BFS with only a queue and dictionary (used as visited set)
        """
        __ node __ N..
            r.. N..
        queue    # list
        start_node = node
        start_cloned_node = UndirectedGraphNode(node.label)
        d = {node: start_cloned_node}
        queue.a..(node)
        i = 0
        w.... i < l..(queue
            node = queue[i]
            i += 1
            ___ neighbor __ node.neighbors:
                __ neighbor n.. __ d:
                    queue.a..(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = cloned_neighbor
        ___ node __ queue:
            cloned_node = d[node]
            cloned_neighbors    # list
            ___ neighbor __ node.neighbors:
                cloned_neighbor = d[neighbor]
                cloned_neighbors.a..(cloned_neighbor)
            cloned_node.neighbors = cloned_neighbors
        r.. d[start_node]
