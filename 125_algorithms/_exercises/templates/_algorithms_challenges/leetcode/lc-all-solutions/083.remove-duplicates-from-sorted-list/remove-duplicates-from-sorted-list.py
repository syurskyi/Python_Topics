# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ deleteDuplicates(self, head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(None)
    dummy.next = head
    p = dummy

    w___ p and p.next:
      __ p.val __ p.next.val:
        p.next = p.next.next
      ____
        p = p.next
    r_ dummy.next
