#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ maxDepth  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r_ 0

        node_list = [root]
        depth_count = 1
        # Breadth-first Search
        _____ node_list:
            # node_scan: all the nodes in one level.
            # Traverse node_scan and get all the nodes of next level,
            # Then update node_list
            node_scan = node_list[:]
            node_list   # list
            ___ node __ node_scan:
                l_child = node.left
                r_child = node.right
                __ l_child:
                    node_list.a.. l_child)
                __ r_child:
                    node_list.a.. r_child)
            __ node_list:
                depth_count += 1

        r_ depth_count
"""
[]
[1]
[1,2,3]
[0,1,2,3,4,5,6,null,null,7,null,8,9,null,10]
"""
