# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    __ head:
      fast = slow = head
      pre = None

      while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next

      __ not pre:
        return head
      pre.next = None

      left = self.sortList(head)
      right = self.sortList(slow)

      p = dummy = ListNode(-1)
      while left and right:
        __ left.val < right.val:
          p.next = left
          left = left.next
        else:
          p.next = right
          right = right.next
        p = p.next

      __ left:
        p.next = left
      __ right:
        p.next = right
      return dummy.next
