# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ rotateRight(self, head, k
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    __ not head:
      r_ head
    l = 1
    p = head
    w___ p.next:
      l += 1
      p = p.next
    k = k % l
    __ k __ 0:
      r_ head
    k = l - k % l - 1
    pp = head
    print
    k
    w___ k > 0:
      pp = pp.next
      k -= 1
    newHead = pp.next
    pp.next = None
    p.next = head
    r_ newHead
