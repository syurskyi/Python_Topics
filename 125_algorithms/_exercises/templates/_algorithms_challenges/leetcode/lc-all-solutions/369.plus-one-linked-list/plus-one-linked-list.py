# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ plusOne(self, head
    """
    :type head: ListNode
    :rtype: ListNode
    """

    ___ reverse(cur
      pre = None
      w___ cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      r_ pre

    p = head = reverse(head)
    carry = 1
    pre = None
    w___ p:
      val = (p.val + carry) % 10
      carry = 1 __ val < p.val else 0
      p.val = val
      pre = p
      p = p.next

    __ carry __ 1:
      pre.next = ListNode(1)
    r_ reverse(head)
