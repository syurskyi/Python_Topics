# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ rotateRight  head, k
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    __ n.. head:
      r.. head
    l = 1
    p = head
    w.... p.next:
      l += 1
      p = p.next
    k = k % l
    __ k __ 0:
      r.. head
    k = l - k % l - 1
    pp = head
    print
    k
    w.... k > 0:
      pp = pp.next
      k -_ 1
    newHead = pp.next
    pp.next = N..
    p.next = head
    r.. newHead
