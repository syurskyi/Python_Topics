#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ generateTrees  n
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        __ n.. n:
            r_ [[]]
        roots_lsit = self.root_list(1, n)
        r_ roots_lsit

    # Get all the roots of the BST's that store values start...end
    ___ root_list  start, end
        # Null Tree when start > end
        __ start > end:
            r_ []
        # Tree has just a root when start==end
        __ start __ end:
            r_ [TreeNode(start)]

        roots   # list
        ___ i __ r..(start, end + 1
            # Get all the possible roots and it's left, right childs
            left_childs = self.root_list(start, i-1)
            right_childs = self.root_list(i+1, end)
            # Have no left childs
            __ n.. left_childs and right_childs:
                ___ child __ right_childs:
                    root_node = TreeNode(i)
                    root_node.right = child
                    root_node.left = None
                    roots.append(root_node)
            # Have no right childs
            ____ n.. right_childs and left_childs:
                ___ child __ left_childs:
                    root_node = TreeNode(i)
                    root_node.left = child
                    root_node.right = None
                    roots.append(root_node)
            # Have both left childs and right childs
            ____
                ___ l_child __ left_childs:
                    ___ r_child __ right_childs:
                        root_node = TreeNode(i)
                        root_node.left = l_child
                        root_node.right = r_child
                        roots.append(root_node)

        r_ roots

"""
0
1
2
3
7
"""
