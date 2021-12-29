# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    ___ r(root):
      pre = N..
      cur = root
      while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      r.. pre

    p = dummy = ListNode(-1)
    p1, p2 = r(l1), r(l2)
    pre = N..
    carry = 0
    while p1 and p2:
      p.next = ListNode(p1.val + p2.val + carry)
      carry = 1 __ p.next.val > 9 ____ 0
      p.next.val = p.next.val % 10
      p1 = p1.next
      p2 = p2.next
      p = p.next
    pp = p1 o. p2
    while pp:
      p.next = ListNode(pp.val + carry)
      carry = 1 __ p.next.val > 9 ____ 0
      p.next.val = p.next.val % 10
      pp = pp.next
      p = p.next
    head = r(dummy.next)
    __ carry:
      n = ListNode(1)
      n.next = head
      head = n
    r.. head
