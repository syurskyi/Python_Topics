# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    ___ removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans

        ___ i __ ra..(1,n+2
            first = first.next
        
        w___ (first is not None
            first = first.next
            second = second.next

        second.next = second.next.next
        

        r_ ans.next
