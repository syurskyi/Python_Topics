# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ oddEvenList  head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    o = odd = ListNode(-1)
    e = even = ListNode(-1)
    p = head
    isOdd = T..
    w.... p:
      __ isOdd:
        o.next = p
        o = o.next
        isOdd = F..
      ____
        e.next = p
        isOdd = T..
        e = e.next
      p = p.next
    e.next = N..
    o.next = even.next
    r.. odd.next
