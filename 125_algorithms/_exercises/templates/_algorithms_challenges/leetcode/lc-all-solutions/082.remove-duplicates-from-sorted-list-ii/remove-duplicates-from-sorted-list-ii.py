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
    dummy = ListNode(-1)
    dummy.next = head
    p = dummy
    w___ p.next:
      __ p.next.next and p.next.val __ p.next.next.val:
        z = p.next
        w___ z and z.next and z.val __ z.next.val:
          z = z.next
        p.next = z.next
      ____
        p = p.next
    r_ dummy.next
