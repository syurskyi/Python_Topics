# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ plusOne(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    ___ reverse(cur):
      pre = N..
      w.... cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      r.. pre

    p = head = reverse(head)
    carry = 1
    pre = N..
    w.... p:
      val = (p.val + carry) % 10
      carry = 1 __ val < p.val ____ 0
      p.val = val
      pre = p
      p = p.next

    __ carry __ 1:
      pre.next = ListNode(1)
    r.. reverse(head)
