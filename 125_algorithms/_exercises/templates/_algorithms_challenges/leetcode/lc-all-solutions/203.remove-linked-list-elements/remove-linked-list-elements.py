# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ removeElements  head, val
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    p = dummy
    w.... p.next:
      __ p.next.val __ val:
        p.next = p.next.next
      ____:
        p = p.next
    r.. dummy.next
