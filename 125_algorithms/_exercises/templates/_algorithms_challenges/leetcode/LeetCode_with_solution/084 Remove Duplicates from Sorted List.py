"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution:
    ___ deleteDuplicates(self, head):
        """
        Two pointers, closed_ptr and open_ptr, to find the next non-duplicate
        O(n)
        :param head: ListNode
        :return: ListNode
        """
        # trivial
        __ n.. head:
            r.. head
        # main
        closed_ptr = head
        open_ptr = head.next
        w.... open_ptr:
            # find the non-duplicate
            w.... open_ptr a.. closed_ptr.val__open_ptr.val:
                open_ptr = open_ptr.next

            closed_ptr.next = open_ptr
            closed_ptr = closed_ptr.next
            open_ptr = open_ptr.next __ open_ptr ____ N..

        r.. head

__ __name____"__main__":
    nodes = [ListNode(1) ___ _ __ r..(2)]
    ___ i __ r..(l..(nodes)-1):
        nodes[i].next = nodes[i+1]

    Solution().deleteDuplicates(nodes[0])