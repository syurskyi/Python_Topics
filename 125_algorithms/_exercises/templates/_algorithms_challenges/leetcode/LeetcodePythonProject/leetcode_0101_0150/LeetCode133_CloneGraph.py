'''
Created on Feb 8, 2017

@author: MT
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    ___ __init__(self, x
        self.label = x
        self.neighbors =   # list

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    ___ cloneGraph(self, node
        __ not node: r_ node
        newHead = UndirectedGraphNode(node.label)
        hashmap = {node:newHead}
        queue = [node]
        w___ queue:
            node = queue.pop(0)
            nodeCopy = hashmap[node]
            ___ node0 __ node.neighbors:
                __ node0 __ hashmap:
                    nodeCopy.neighbors.append(hashmap[node0])
                ____
                    node0Copy = UndirectedGraphNode(node0.label)
                    hashmap[node0] = node0Copy
                    nodeCopy.neighbors.append(node0Copy)
                    queue.append(node0)
        r_ newHead
