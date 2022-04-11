#!/usr/bin/python3
"""
Given the root of a binary tree, then value v and depth d, you need to add a row
of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree
nodes N in depth d-1, create two tree nodes with value v as N's left subtree
root and right subtree root. And N's original left subtree should be the left
subtree of the new left subtree root, its original right subtree should be the
right subtree of the new right subtree root. If depth d is 1 that means there is
no depth d-1 at all, then create a tree node with value v as the new root of the
whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:
Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ addOneRow  root: TreeNode, v: i.., d: i..) __ TreeNode:
        r.. add(root, v, d, 1, "left")

    ___ add  node, v, d, cur_d, child) __ TreeNode:
        # use the return value for parent's reference 
        __ cur_d __ d:
            new TreeNode(v)
            setattr(new, child, node)
            r.. new

        __ node:
            node.left add(node.left, v, d, cur_d + 1, "left")
            node.right add(node.right, v, d, cur_d + 1, "right")
            r.. node


c_ Solution2:
    ___ addOneRow  root: TreeNode, v: i.., d: i..) __ TreeNode:
        __ d __ 1:
            node TreeNode(v)
            node.left root
            r.. node

        add  root, v, d, 1)
        r.. root

    ___ add  node, v, d, cur_d) __ N..
        __ n.. node:
            r..

        __ cur_d + 1 __ d:
            left node.left
            right node.right
            node.left TreeNode(v)
            node.left.left left
            node.right TreeNode(v)
            node.right.right right

        add(node.left, v, d, cur_d + 1)
        add(node.right, v, d, cur_d + 1)
