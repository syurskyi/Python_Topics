# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ partition  head, x
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    __ head __ N..
      r.. N..
    dummy = ListNode(-1)
    dummy.next = head
    sHead = sDummy = ListNode(-1)
    p = dummy
    w.... p a.. p.next:
      __ p.next.val < x:
        sDummy.next = p.next
        p.next = p.next.next
        sDummy = sDummy.next
      ____:
        p = p.next
      # if you change p.next then make sure you wouldn't change p in next run
    sDummy.next = dummy.next
    r.. sHead.next
