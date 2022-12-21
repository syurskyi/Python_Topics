#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


c.. Solution o..
    ___ reorderList  head
        """
        Firstly, use two pointer to find the mid node_keep,
        Then reverse the post half nodes, and merge the pre half and
        post reversed half.
        """
        __ n.. head or n.. head.next or n.. head.next.next:
            r_
        slow = fast = head
        _____ fast.next:
            __ fast.next.next:
                slow = slow.next
                fast = fast.next.next
            ____
                break

        post_half_start = slow.next
        slow.next = None
        reverse_head = self.reverse_list(post_half_start)
        _____ head and reverse_head:
            node_keep = head.next
            reverse_node_keep = reverse_head.next
            head.next = reverse_head
            reverse_head.next = node_keep
            head = node_keep
            reverse_head = reverse_node_keep

    # Reverse a linked list
    ___ reverse_list  head
        pre_node = None
        post_node = None
        _____ head:
            post_node = head.next
            head.next = pre_node
            pre_node = head
            head = post_node

        r_ pre_node

    # RuntimeError: maximum recursion depth exceeded
    """
    def reverse_list(self, head):
        if not head.next:
            return head
        next_node = head.next
        new_head = self.reverse_list(next_node)
        next_node.next = head
        head.next = None
        return new_head
    """

"""
[]
[1]
[1,2]
[1,2,3,4,5,6]
[1,2,3,4,5]
"""
