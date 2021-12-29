#!/usr/bin/python3
"""
We are given the head node root of a binary tree, where additionally every
node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1
has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant
of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]



Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.
"""


# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


____ typing _______ Tuple


class Solution:
    ___ pruneTree(self, root: TreeNode) -> TreeNode:
        root, _ = self.prune(root)
        r.. root

    ___ prune(self, node) -> Tuple[TreeNode, bool]:
        __ n.. node:
            r.. N.., False

        node.left, contain_left = self.prune(node.left)
        node.right, contain_right = self.prune(node.right)
        __ n.. contain_left a.. n.. contain_right a.. node.val __ 0:
            r.. N.., False

        r.. node, True
