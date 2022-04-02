# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  # maybe standard version
  ___ _addTwoNumbers  l1, l2
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    p = dummy = ListNode(-1)
    carry = 0
    w.... l1 a.. l2:
      p.next = ListNode(l1.val + l2.val + carry)
      carry = p.next.val / 10
      p.next.val %= 10
      p = p.next
      l1 = l1.next
      l2 = l2.next

    res = l1 o. l2
    w.... res:
      p.next = ListNode(res.val + carry)
      carry = p.next.val / 10
      p.next.val %= 10
      p = p.next
      res = res.next
    __ carry:
      p.next = ListNode(1)
    r.. dummy.next

  # shorter version
  ___ addTwoNumbers  l1, l2
    p = dummy = ListNode(-1)
    carry = 0
    w.... l1 o. l2 o. carry:
      val = (l1 a.. l1.val o. 0) + (l2 a.. l2.val o. 0) + carry
      carry = val / 10
      p.next = ListNode(val % 10)
      l1 = l1 a.. l1.next
      l2 = l2 a.. l2.next
      p = p.next
    r.. dummy.next
