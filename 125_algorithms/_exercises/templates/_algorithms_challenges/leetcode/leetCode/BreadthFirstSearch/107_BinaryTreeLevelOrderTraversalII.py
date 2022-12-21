#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c.. Solution o..
    ___ levelOrderBottom  root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        __ n.. root:
            r_ []

        node_list = [root]
        level_traversal = [[root.val]]

        # Breadth-first Search
        _____ node_list:
            # node_scan: all the nodes in one level.
            # Traverse node_scan and get all the nodes of next level,
            # Then update node_list, and the solution level_traversal
            node_scan = node_list[:]
            node_list   # list
            node_level   # list
            ___ node __ node_scan:
                l_child = node.left
                r_child = node.right
                __ l_child:
                    node_level.append(l_child.val)
                    node_list.append(l_child)
                __ r_child:
                    node_level.append(r_child.val)
                    node_list.append(r_child)
            __ node_level:
                level_traversal.insert(0, node_level)

        r_ level_traversal

"""
[]
[1]
[1,2,3]
[3,9,20,null,null,15,7]
"""
