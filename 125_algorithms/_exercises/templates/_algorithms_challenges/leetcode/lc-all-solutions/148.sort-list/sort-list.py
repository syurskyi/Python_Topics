# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ sortList  head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    __ head:
      fast = slow = head
      pre = N..

      w.... fast a.. fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next

      __ n.. pre:
        r.. head
      pre.next = N..

      left = sortList(head)
      right = sortList(slow)

      p = dummy = ListNode(-1)
      w.... left a.. right:
        __ left.val < right.val:
          p.next = left
          left = left.next
        ____:
          p.next = right
          right = right.next
        p = p.next

      __ left:
        p.next = left
      __ right:
        p.next = right
      r.. dummy.next
