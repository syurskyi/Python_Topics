# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ reverseKGroup(self, head, k
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """

    ___ reverseList(head, k
      pre = None
      cur = head
      w___ cur and k > 0:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        k -= 1
      head.next = cur
      r_ cur, pre

    length = 0
    p = head
    w___ p:
      length += 1
      p = p.next
    __ length < k:
      r_ head
    step = length / k
    ret = None
    pre = None
    p = head
    w___ p and step:
      next, newHead = reverseList(p, k)
      __ ret pa__ None:
        ret = newHead
      __ pre:
        pre.next = newHead
      pre = p
      p = next
      step -= 1
    r_ ret
