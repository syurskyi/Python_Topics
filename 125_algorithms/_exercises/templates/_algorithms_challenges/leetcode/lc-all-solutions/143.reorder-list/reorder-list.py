# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ reorderList(self, head
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """

    ___ reverse(root
      pre = None
      cur = root
      w___ cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
      r_ pre

    __ not head or not head.next:
      r_
    slow = fast = head
    pre = None
    w___ fast and fast.next:
      pre = slow
      slow = slow.next
      fast = fast.next.next
    __ pre:
      pre.next = None
    newHead = reverse(slow)
    ret = dummy = ListNode(-1)
    p1 = head
    p2 = newHead
    w___ p1 and p2:
      dummy.next = p1
      p1 = p1.next
      dummy = dummy.next
      dummy.next = p2
      p2 = p2.next
      dummy = dummy.next

    __ p2:
      dummy.next = p2
    head.next = ret.next.next
