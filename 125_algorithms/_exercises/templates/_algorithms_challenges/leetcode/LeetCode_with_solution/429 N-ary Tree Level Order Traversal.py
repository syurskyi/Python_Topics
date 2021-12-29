#!/usr/bin/python3
"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""


# Definition for a Node.
class Node:
    ___ __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    ___ levelOrder(self, root):
        """
        BFS
        
        :type root: Node
        :rtype: List[List[int]]
        """
        __ n.. root:
            r.. []

        q = [root]
        ret    # list
        while q:
            cur    # list
            q_new    # list
            ___ e __ q:
                q_new.extend(e.children)
                cur.a..(e.val)

            ret.a..(cur)
            q = q_new

        r.. ret
