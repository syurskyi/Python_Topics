# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ oddEvenList(self, head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    o = odd = ListNode(-1)
    e = even = ListNode(-1)
    p = head
    isOdd = True
    w___ p:
      __ isOdd:
        o.next = p
        o = o.next
        isOdd = False
      ____
        e.next = p
        isOdd = True
        e = e.next
      p = p.next
    e.next = None
    o.next = even.next
    r_ odd.next
