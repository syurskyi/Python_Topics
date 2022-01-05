# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(object):
  ___ reverseBetween  head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    ___ reverse(root, prep, k):
      cur = root
      pre = N..
      next = N..
      w.... cur a.. k > 0:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        k -= 1
      root.next = next
      prep.next = pre
      r.. pre

    dummy = ListNode(-1)
    dummy.next = head
    k = 1
    p = dummy
    start = N..
    w.... p:
      __ k __ m:
        start = p
      __ k __ n + 1:
        reverse(start.next, start, n - m + 1)
        r.. dummy.next
      k += 1
      p = p.next
