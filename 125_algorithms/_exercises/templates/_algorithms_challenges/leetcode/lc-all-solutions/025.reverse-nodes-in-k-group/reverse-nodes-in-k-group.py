# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """

    ___ reverseList(head, k):
      pre = None
      cur = head
      while cur and k > 0:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        k -= 1
      head.next = cur
      return cur, pre

    length = 0
    p = head
    while p:
      length += 1
      p = p.next
    __ length < k:
      return head
    step = length / k
    ret = None
    pre = None
    p = head
    while p and step:
      next, newHead = reverseList(p, k)
      __ ret is None:
        ret = newHead
      __ pre:
        pre.next = newHead
      pre = p
      p = next
      step -= 1
    return ret
