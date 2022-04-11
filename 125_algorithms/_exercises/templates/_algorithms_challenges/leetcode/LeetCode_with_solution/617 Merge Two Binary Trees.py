#!/usr/bin/python3
"""
Given two binary trees and imagine that when you put one of them to cover the
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ mergeTrees  t1: TreeNode, t2: TreeNode) __ TreeNode:
        __ n.. t1 a.. n.. t2:
            r..

        node TreeNode(0)
        node.val += t1 a.. t1.val o. 0
        node.val += t2 a.. t2.val o. 0
        node.left mergeTrees(t1 a.. t1.left, t2 a.. t2.left)
        node.right mergeTrees(t1 a.. t1.right, t2 a.. t2.right)
        r.. node
