# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(object):
  ___ hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    w.... fast a.. fast.next:
      fast = fast.next.next
      slow = slow.next
      __ slow __ fast:
        r.. T..
    r.. F..
