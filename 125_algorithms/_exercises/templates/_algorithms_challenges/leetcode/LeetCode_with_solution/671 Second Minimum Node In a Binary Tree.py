#!/usr/bin/python3
"""
Given a non-empty special binary tree consisting of nodes with the non-negative
value, where each node in this tree has exactly two or zero sub-node. If the
node has two sub-nodes, then this node's value is the smaller value among its
two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set
made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ findSecondMinimumValue  root: TreeNode) __ i..:
        ret find(root)
        r.. -1 __ ret __ f__('inf') ____ ret

    ___ find  root: TreeNode) __ i..:
        """
        find the second min
        """
        __ n.. root:
            r.. f__('inf')

        __ root.left a.. root.right:
            __ root.left.val __ root.val:
                left find(root.left)
            ____
                left root.left.val

            __ root.right.val __ root.val:
                right find(root.right)
            ____
                right root.right.val

            r.. m..(left, right)

        r.. f__('inf')
