# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ reorderList(self, head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """

    ___ reverse(root):
      pre = N..
      cur = root
      w.... cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
      r.. pre

    __ n.. head o. n.. head.next:
      r..
    slow = fast = head
    pre = N..
    w.... fast a.. fast.next:
      pre = slow
      slow = slow.next
      fast = fast.next.next
    __ pre:
      pre.next = N..
    newHead = reverse(slow)
    ret = dummy = ListNode(-1)
    p1 = head
    p2 = newHead
    w.... p1 a.. p2:
      dummy.next = p1
      p1 = p1.next
      dummy = dummy.next
      dummy.next = p2
      p2 = p2.next
      dummy = dummy.next

    __ p2:
      dummy.next = p2
    head.next = ret.next.next
