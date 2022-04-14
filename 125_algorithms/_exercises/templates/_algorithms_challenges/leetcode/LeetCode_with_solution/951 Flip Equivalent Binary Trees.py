#!/usr/bin/python3
"""
For a binary tree T, we can define a flip operation as follows: choose any node,
and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make
X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.
The trees are given by root nodes root1 and root2.



Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram


Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].
"""

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ flipEquiv  root1: TreeNode, root2: TreeNode) __ b..
        """
        O(N)
        """
        __ n.. root1 a.. n.. root2:
            r.. T..
        ____ n.. root1 o. n.. root2:
            r.. F..

        __ root1.val !_ root2.val:
            r.. F..

        r.. flipEquiv(root1.left, root2.left) a.. flipEquiv(root1.right, root2.right) o. \
            flipEquiv(root1.left, root2.right) a.. flipEquiv(root1.right, root2.left)
