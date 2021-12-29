"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should
become 1 -> 2 -> 4 after calling your function.
"""
__author__ = 'Daniel'


class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    ___ deleteNode(self, node):
        """
        Only access to the node to be deleted.
        :param node: ListNode
        :return: None, Do not return anything, modify node in-place instead.
        """
        cur = node
        while cur.next:
            cur.val = cur.next.val
            __ not cur.next.next:
                cur.next = None
                break

            cur = cur.next