# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    __ not head:
      return head
    l = 1
    p = head
    while p.next:
      l += 1
      p = p.next
    k = k % l
    __ k == 0:
      return head
    k = l - k % l - 1
    pp = head
    print
    k
    while k > 0:
      pp = pp.next
      k -= 1
    newHead = pp.next
    pp.next = None
    p.next = head
    return newHead
