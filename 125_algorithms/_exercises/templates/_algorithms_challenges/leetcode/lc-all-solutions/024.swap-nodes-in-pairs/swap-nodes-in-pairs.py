# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ swapPairs(self, head
    """
    :type head: ListNode
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

    __ not head or not head.next:
      r_ head
    ret = head.next
    p = head
    pre = None
    w___ p:
      next, newHead = reverseList(p, 2)
      __ pre:
        pre.next = newHead
      pre = p
      p = next
    r_ ret
