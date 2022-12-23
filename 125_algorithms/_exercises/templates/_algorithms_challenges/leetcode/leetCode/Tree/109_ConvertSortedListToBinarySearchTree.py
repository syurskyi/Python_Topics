#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ sortedListToBST  head
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums   # list
        _____ head:
            nums.a.. head.val)
            head = head.next
        __ n.. nums:
            r_ None
        r_ self.get_root(nums)

    ___ get_root  nums
        __ n.. nums:
            r_ None
        nums_l = l..(nums)
        __ nums_l __ 1:
            r_ TreeNode(nums[0])

        # Find the root of the current balanced BST,
        # which is conconverted by the current nums.
        root_index = nums_l / 2
        root = TreeNode(nums[root_index])
        root.left = self.get_root(nums[:root_index])
        root.right = self.get_root(nums[root_index+1:])
        r_ root

"""
[]
[1,3,5,7]
[1,3,5,7,9,11]
[1,3,5,7,9,11,13]
"""
