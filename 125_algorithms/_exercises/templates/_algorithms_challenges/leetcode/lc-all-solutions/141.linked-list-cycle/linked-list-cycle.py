# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ hasCycle(self, head
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    w___ fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      __ slow __ fast:
        r_ True
    r_ False
