"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

删除所有的val。

注意下开头即为 val 的情况。

beat
90%

测试地址：
https://leetcode.com/problems/remove-linked-list-elements/description/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    ___ removeElements  head, val
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        _____ head:
            __ head.val __ val:
                head = head.next
            ____
                ______
        
        _head = head
        
        __ n.. _head:
            r_ None
        
        _____ head a.. head.next:
            __ head.next.val __ val:
                head.next = head.next.next
            ____
                head = head.next
        r_ _head
