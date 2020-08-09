# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    ___ addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        pointer = ans

        carry = 0
        su. = 0

        w___(l1!=None or l2!=None
            su. = carry
            __(l1!=None
                su.+=l1.val
                l1 = l1.next
            __(l2!=None
                su.+=l2.val
                l2 = l2.val
            
            carry = int(su./10)
            pointer.next  = ListNode(su.%10)

            pointer = pointer.next
        
        __(carry>0
            pointer.next = ListNode(carry)
        
        r_ ans.next