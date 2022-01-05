# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(object):
  ___ detectCycle  head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow = fast = finder = head
    w.... fast a.. fast.next:
      slow = slow.next
      fast = fast.next.next
      __ slow __ fast:
        w.... finder != slow:
          finder = finder.next
          slow = slow.next
        r.. finder
    r.. N..
