# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    ___ oddEvenList(self, head: ListNode) -> ListNode:
        __(not head
            r_ head

        odd = head
        even = odd.next
        evenList = even

        w___(even and even.next
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenList
        r_ head