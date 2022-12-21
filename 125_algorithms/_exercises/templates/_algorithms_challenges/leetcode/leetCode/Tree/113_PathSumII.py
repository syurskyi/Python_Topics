#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ pathSum  root, s..
        __ n.. root:
            r_ []
        paths_list   # list
        __ n.. root.left and n.. root.right:
            __ root.val __ s..:
                paths_list.append([root.val])
            r_ paths_list

        __ root.left:
            l_paths = self.pathSum(root.left, s..-root.val)
            # There are paths along root.left
            __ l_paths:
                ___ path __ l_paths:
                    one_path = [root.val]
                    one_path.e..(path)
                    paths_list.append(one_path)

        __ root.right:
            r_paths = self.pathSum(root.right, s..-root.val)
            # There are paths along root.right
            __ r_paths:
                ___ path __ r_paths:
                    one_path = [root.val]
                    one_path.e..(path)
                    paths_list.append(one_path)
        r_ paths_list


# Pythonic way.  So short and beautiful!
c.. Solution_2 o..
    ___ pathSum  root, s..
        __ n.. root:
            r_ []
        __ n.. root.left and n.. root.right and s.. __ root.val:
            r_ [[root.val]]
        tmp = (self.pathSum(root.left, s..-root.val) +
               self.pathSum(root.right, s..-root.val))
        r_ [[root.val] + i ___ i __ tmp]


"""
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,3,3,3]
6
"""
