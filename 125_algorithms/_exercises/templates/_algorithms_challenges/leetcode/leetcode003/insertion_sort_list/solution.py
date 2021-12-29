# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    ___ insertionSortList(self, head):
        h = head  # h is the temporary head node
        # First node of h
        __ head __ n.. N..
            head = head.next
            h.next = N..
        while head __ n.. N..
            next_node = head.next
            # Insertion sort
            current = h
            prev = h
            while current __ n.. N.. and head.val > current.val:
                prev = current
                current = current.next
            # head is smaller than the head node of h
            # Insert head to the beginning of h
            __ prev __ current:
                head.next = h
                h = head
            # Insert head to the middle or end of h
            ____:
                prev.next = head
                head.next = current
            head = next_node
        r.. h
