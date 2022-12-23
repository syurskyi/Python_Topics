"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

无脑怼。

beat:
99%.

测试地址：
https://leetcode.com/problems/partition-list/description/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    ___ partition  head, x
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        all_nodes   # list
        
        _____ head:
            all_nodes.a.. head.val)
            head = head.next
        
        less_nodes   # list
        greater_nodes   # list
        
        ___ i __ all_nodes:
            __ i < x:
                less_nodes.a.. i)
            ____
                greater_nodes.a.. i)
        
        __ less_nodes:
            less_head = ListNode(less_nodes[0])
        
        head = less_head __ less_nodes else None
        
        ___ i __ less_nodes[1:]:
            less_head.next = ListNode(i)
            less_head = less_head.next
        
        __ greater_nodes:
            greater_head = ListNode(greater_nodes[0])
        
        _head = greater_head __ greater_nodes else None
        
        ___ i __ greater_nodes[1:]:
            greater_head.next = ListNode(i)
            greater_head = greater_head.next
        
        __ head:
            less_head.next = _head
        
            r_ head
        r_ _head
        