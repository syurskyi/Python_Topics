#!/usr/bin/python3
"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""


# Definition for a Node.
c_ Node:
    ___ - , val, children
        val val
        children children


c_ Solution:
    ___ levelOrder  root
        """
        BFS
        
        :type root: Node
        :rtype: List[List[int]]
        """
        __ n.. root:
            r.. []

        q [root]
        ret    # list
        w.... q:
            cur    # list
            q_new    # list
            ___ e __ q:
                q_new.e.. e.children)
                cur.a..(e.val)

            ret.a..(cur)
            q q_new

        r.. ret
