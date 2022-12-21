#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/43771/implemented-java-binary-search-order-iterative-recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Binary search iterative
c.. Solution o..
    ___ kthSmallest  root, k
        count = self.get_nodes(root.left)
        _____ count + 1 != k:
            __ count + 1 < k:
                root = root.right
                k = k - count - 1
            ____
                root = root.left
            count = self.get_nodes(root.left)
        r_ root.val

    ___ get_nodes  root
        __ n.. root:
            r_ 0
        r_ 1 + self.get_nodes(root.left) + self.get_nodes(root.right)


# Binary search recursive
c.. Solution_2 o..
    ___ kthSmallest  root, k
        count = self.get_nodes(root.left)
        __ count+1 < k:
            r_ self.kthSmallest(root.right, k-count-1)
        ____ count+1 __ k:
            r_ root.val
        ____
            r_ self.kthSmallest(root.left, k)

    ___ get_nodes  root
        __ n.. root:
            r_ 0
        r_ 1 + self.get_nodes(root.left) + self.get_nodes(root.right)


# DFS in-order iterative:
c.. Solution_3 o..
    ___ kthSmallest  root, k
        node_stack   # list
        count, result = 0, 0
        _____ root or node_stack:
            __ root:
                node_stack.append(root)
                root = root.left
            ____
                __ node_stack:
                    root = node_stack.pop()
                    result = root.val
                    count += 1
                    __ count __ k:
                        r_ result
                    root = root.right

        r_ -1   # never hit if k is valid


# DFS in-order recursive:
c.. Solution_4 o..
    ___ kthSmallest  root, k
        self.k = k
        self.num = 0
        self.in_order(root)
        r_ self.num

    ___ in_order  root
        __ root.left:
            self.in_order(root.left)
        self.k -= 1
        __ self.k __ 0:
            self.num = root.val
            r_
        __ root.right:
            self.in_order(root.right)


# DFS in-order recursive, Pythonic approach with generator:
c.. Solution_5 o..
    ___ kthSmallest  root, k
        ___ val __ self.in_order(root
            __ k __ 1:
                r_ val
            ____
                k -= 1

    ___ in_order  root
        __ root:
            ___ val __ self.in_order(root.left
                yield val
            yield root.val
            ___ val __ self.in_order(root.right
                yield val

"""
[1]
1
[3,1,4,null,2]
1
[10,8,6,9,14,12,15,null,null,null,null,11]
4
[10,8,6,9,14,12,15,null,null,null,null,11]
5
"""
