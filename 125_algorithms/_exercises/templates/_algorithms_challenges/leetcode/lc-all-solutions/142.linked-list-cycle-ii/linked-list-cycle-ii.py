# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ detectCycle(self, head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow = fast = finder = head
    w___ fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      __ slow __ fast:
        w___ finder != slow:
          finder = finder.next
          slow = slow.next
        r_ finder
    r_ None
