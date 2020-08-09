# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ reverseBetween(self, head, m, n
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    ___ reverse(root, prep, k
      cur = root
      pre = None
      next = None
      w___ cur and k > 0:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        k -= 1
      root.next = next
      prep.next = pre
      r_ pre

    dummy = ListNode(-1)
    dummy.next = head
    k = 1
    p = dummy
    start = None
    w___ p:
      __ k __ m:
        start = p
      __ k __ n + 1:
        reverse(start.next, start, n - m + 1)
        r_ dummy.next
      k += 1
      p = p.next
