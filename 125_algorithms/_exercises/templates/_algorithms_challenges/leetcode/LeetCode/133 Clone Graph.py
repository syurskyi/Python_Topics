"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
__author__ = 'Danyang'
# Definition for a undirected graph node
class UndirectedGraphNode:
    ___ __init__(self, x
        self.label = x
        self.neighbors = []
    ___ __repr__(self
        r_ repr(self.label)

class Solution:
    ___ cloneGraph_TLE(self, node
        """
        dfs
        :param node: UndirectedGraphNode
        :return: UndirectedGraphNode
        """
        r_ self.clone_graph_visited(node, set())

    ___ clone_graph_visited(self, node, visited_set
        """
        post-order traversal
        Time Limit Exceeded
        :param node:
        :param visited_set:
        :return:
        """
        __ not node:
            r_
        visited_set.add(node)
        neighbors_cloned = [self.clone_graph_visited(neighbor, set(visited_set)) ___ neighbor in node.neighbors __ neighbor not in visited_set]
        node_cloned = UndirectedGraphNode(node.label)
        ___ neighbor_cloned in neighbors_cloned:
            __ neighbor_cloned not in visited_set:
                neighbor_cloned.neighbors.append(node_cloned)
        node_cloned.neighbors = neighbors_cloned
        r_ node_cloned

    ___ cloneGraph(self, node
        """
        bfs with visited
        similar to 138 Copy List with Random Pointer

        copy_map: dict, 1. book keeping whether it is coped (visited); 2. reserve for being copied as neighbor, # shadow
        q: list, queue of nodes whose the neighbors are to be copied

        :param node: UndirectedGraphNode
        :return: UndirectedGraphNode
        """
        __ not node:
            r_

        original2copy = {} # dict  #!important
        q = [node]  # queue of nodes whose the neighbors are to be copied

        clone = UndirectedGraphNode(node.label)
        original2copy[node] = clone
        w___ q:
            cur = q.pop()
            ___ neighbor in cur.neighbors:
                __ neighbor in original2copy:  # already copied
                    original2copy[cur].neighbors.append(original2copy[neighbor])
                ____
                    q.append(neighbor)
                    clone_neighbor = UndirectedGraphNode(neighbor.label)
                    original2copy[neighbor] = clone_neighbor
                    original2copy[cur].neighbors.append(original2copy[neighbor])

        r_ original2copy[node]


__ __name____"__main__":
    lst = [UndirectedGraphNode(i+1) ___ i in range(3)]
    ___ item in lst:
        item.neighbors = list(lst)
        item.neighbors.remove(item)
    cloned = Solution().cloneGraph(lst[0])
    assert cloned.neighbors[0].label in (2, 3)
    assert cloned.neighbors[1].label in (2, 3)


