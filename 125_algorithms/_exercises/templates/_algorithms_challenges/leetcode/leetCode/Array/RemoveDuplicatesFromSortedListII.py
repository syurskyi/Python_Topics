"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

这次要把全部的重复都删除。

我的思路是利用标记，过一遍，先把重复的删到剩一个，然后把剩下的一个标记为重复。

然后做一个新的链表。

beat 72%

测试地址：
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    ___ deleteDuplicates  head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head:
            r_ head
        
        x = head
        
        _____ head.next:
            __ head.val __ head.next.val:
                head.next = head.next.next
                head.duplicate = True
            ____
                head = head.next
        
        _____ x:
            __ hasattr(x, 'duplicate'
                x = x.next
            ____
                break      
        
        __ n.. x:
            r_ None
        
        new = ListNode(x.val)
        x = x.next
        _new = new
        
        _____ x:
            __ hasattr(x, 'duplicate'
                x = x.next
            ____
                new.next = ListNode(x.val)
                new = new.next
                x = x.next
        r_ _new
