# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ reverseKGroup  head, k
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """

    ___ reverseList(head, k
      pre = N..
      cur = head
      w.... cur a.. k > 0:
        tmp  cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        k -_ 1
      head.next = cur
      r.. cur, pre

    length = 0
    p = head
    w.... p:
      length += 1
      p = p.next
    __ length < k:
      r.. head
    step = length / k
    ret = N..
    pre = N..
    p = head
    w.... p a.. step:
      next, newHead = reverseList(p, k)
      __ ret __ N..
        ret = newHead
      __ pre:
        pre.next = newHead
      pre = p
      p = next
      step -_ 1
    r.. ret
