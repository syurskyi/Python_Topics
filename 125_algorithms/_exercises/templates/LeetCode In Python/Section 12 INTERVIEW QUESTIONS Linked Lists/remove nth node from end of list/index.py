# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

c_ Solution:
    ___ removeNthFromEnd(, head: ListNode, n: in.)  ListNode:
        ans _ ListNode(0)
        ans.next _ head

        first _ ans
        second _ ans

        ___ i __ ra..(1,n+2
            first _ first.next
        
        w___ (first is no. N..
            first _ first.next
            second _ second.next

        second.next _ second.next.next
        

        r_ ans.next