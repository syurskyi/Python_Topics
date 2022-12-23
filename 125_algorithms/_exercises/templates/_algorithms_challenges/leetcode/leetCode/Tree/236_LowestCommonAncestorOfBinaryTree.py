#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    """
    Recursive method: DFS.
    If the current (sub)tree contains both p and q, then the function result is their LCA.
    If only one of them is in that subtree, then the result is that one of them.
    If neither are in that subtree, the result is null/None/nil.

    More version can be found here:
    https://discuss.leetcode.com/topic/18561/4-lines-c-java-python-ruby
    """
    ___ lowestCommonAncestor  root, p, q
        __ n.. root or root __ p or root __ q:
            r_ root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if p and q are on both sides
        __ left a.. right:
            r_ root
        ____
            r_ left or right


c.. Solution_2 o..
    """
    Iterative method: BFS(DFS is ok too).  According to:
    https://leetcode.com/discuss/64764/java-python-iterative-solution
    """
    ___ lowestCommonAncestor  root, p, q
        node_stack = [root]
        parent_record = {root: None}

        # Build the relationship from child to parent
        _____ p n.. __ parent_record or q n.. __ parent_record:
            node = node_stack.pop()
            __ node.left:
                node_stack.a.. node.left)
                parent_record[node.left] = node
            __ node.right:
                node_stack.a.. node.right)
                parent_record[node.right] = node

        # Trace brack from one node, record the path.
        # Then trace from the other.
        ancestors = s..()
        _____ p:
            ancestors.add(p)
            p = parent_record[p]

        _____ q n.. __ ancestors:
            q = parent_record[q]
        r_ q
