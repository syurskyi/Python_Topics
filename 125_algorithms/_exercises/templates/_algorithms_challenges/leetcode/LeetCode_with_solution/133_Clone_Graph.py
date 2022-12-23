# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

c_ Solution o..

    # def __init__(self):
    #     self.label_map = {}

    # def cloneGraph(self, node):
    #     """
    #     :type node: UndirectedGraphNode
    #     :rtype: UndirectedGraphNode
    #     """
    #     # DFS
    #     if node is None:
    #         return None
    #     res = UndirectedGraphNode(node.label)
    #     self.label_map[node.label] = res
    #     for ne in node.neighbors:
    #         if ne.label not in self.label_map:
    #             res.neighbors.append(self.cloneGraph(ne))
    #         else:
    #             res.neighbors.append(self.label_map[ne.label])
    #     return res

    ___ cloneGraph  node
        # BFS
        __ node is N..:
            r_ N..
        label_map  # dict
        queue = [node]
        graphCopy = UndirectedGraphNode(node.label)
        label_map[node.label] = graphCopy
        w.. l.. queue) > 0:
            curr = queue.pop(0)
            ___ ne __ curr.neighbors:
                __ ne.label __ label_map:
                    label_map[curr.label].neighbors.a.. label_map[ne.label])
                ____
                    neighborCopy = UndirectedGraphNode(ne.label)
                    label_map[curr.label].neighbors.a.. neighborCopy)
                    label_map[ne.label] = neighborCopy
                    queue.a.. ne)
        r_ graphCopy

