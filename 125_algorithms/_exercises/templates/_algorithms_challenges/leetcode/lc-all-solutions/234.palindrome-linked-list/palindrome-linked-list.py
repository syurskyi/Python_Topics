# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  ___ isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    ___ reverseList(root):
      pre = N..
      cur = root
      while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      r.. pre

    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    newHead = reverseList(slow)
    p1 = head
    p2 = newHead
    while p1 and p2:
      __ p1.val != p2.val:
        r.. False
      p1 = p1.next
      p2 = p2.next
    r.. True
