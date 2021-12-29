# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    ___ reverseList(head, k):
      pre = N..
      cur = head
      while cur and k > 0:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        k -= 1
      head.next = cur
      r.. cur, pre

    __ n.. head o. n.. head.next:
      r.. head
    ret = head.next
    p = head
    pre = N..
    while p:
      next, newHead = reverseList(p, 2)
      __ pre:
        pre.next = newHead
      pre = p
      p = next
    r.. ret
