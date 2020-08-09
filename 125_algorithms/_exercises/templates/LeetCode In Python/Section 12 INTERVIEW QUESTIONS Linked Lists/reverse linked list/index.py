# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None


class Solution:
    ___ reverseList(self, head: ListNode) -> ListNode:
        node = None
        w___(head is not None
            next = head.next
            head.next = node
            node = head
            head = next
        r_ node
