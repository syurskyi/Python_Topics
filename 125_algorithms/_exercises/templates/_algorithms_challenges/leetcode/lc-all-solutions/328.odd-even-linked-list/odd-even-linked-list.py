# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    o = odd = ListNode(-1)
    e = even = ListNode(-1)
    p = head
    isOdd = True
    while p:
      __ isOdd:
        o.next = p
        o = o.next
        isOdd = False
      ____:
        e.next = p
        isOdd = True
        e = e.next
      p = p.next
    e.next = N..
    o.next = even.next
    r.. odd.next
