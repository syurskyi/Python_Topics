'''
Created on Feb 8, 2017

@author: MT
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    ___ __init__(self, x):
        self.label = x
        self.neighbors    # list

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    ___ cloneGraph(self, node):
        __ n.. node: r.. node
        newHead = UndirectedGraphNode(node.label)
        hashmap = {node:newHead}
        queue = [node]
        while queue:
            node = queue.pop(0)
            nodeCopy = hashmap[node]
            ___ node0 __ node.neighbors:
                __ node0 __ hashmap:
                    nodeCopy.neighbors.a..(hashmap[node0])
                ____:
                    node0Copy = UndirectedGraphNode(node0.label)
                    hashmap[node0] = node0Copy
                    nodeCopy.neighbors.a..(node0Copy)
                    queue.a..(node0)
        r.. newHead
