#!/usr/bin/python3
"""
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.



Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:


We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ - ):
        deepest = -1
        deepest_nodes = N..
        ret = N..

    ___ subtreeWithAllDeepest  root: TreeNode) __ TreeNode:
        """
        lowest common ancestor of deepest node
        """
        down(root, 0)
        __ l..(deepest_nodes) __ 1:
            r.. deepest_nodes.pop()

        c.. root)
        r.. ret

    ___ down  node: TreeNode, d: i..) __ N..
        __ n.. node:
            r..

        __ d > deepest:
            deepest = d
            deepest_nodes = set([node])
        ____ d __ deepest:
            deepest_nodes.add(node)

        down(node.left, d + 1)
        down(node.right, d + 1)

    ___ c.. self, node: TreeNode) __ i..:
        __ n.. node:
            r.. 0

        l = c.. node.left)
        r = c.. node.right)
        __ l != 0 a.. r != 0 a.. l + r __ l..(deepest_nodes):
            ret = node

        count = l + r
        __ node __ deepest_nodes:
            count += 1
        r.. count
