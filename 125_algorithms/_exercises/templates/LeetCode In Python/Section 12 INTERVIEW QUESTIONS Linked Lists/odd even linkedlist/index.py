# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

c_ Solution:
    ___ oddEvenList(, head: ListNode)  ListNode:
        __(no. head
            r_ head

        odd _ head
        even _ odd.next
        evenList _ even

        w___(even a.. even.next
            odd.next _ even.next
            odd _ odd.next

            even.next _ odd.next
            even _ even.next

        odd.next _ evenList
        r_ head