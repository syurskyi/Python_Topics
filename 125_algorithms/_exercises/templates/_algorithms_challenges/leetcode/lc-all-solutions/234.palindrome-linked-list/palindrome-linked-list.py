# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..):
  ___ isPalindrome  head):
    """
    :type head: ListNode
    :rtype: bool
    """

    ___ reverseList(root):
      pre = N..
      cur = root
      w.... cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      r.. pre

    slow = fast = head
    w.... fast a.. fast.next:
      slow = slow.next
      fast = fast.next.next

    newHead = reverseList(slow)
    p1 = head
    p2 = newHead
    w.... p1 a.. p2:
      __ p1.val != p2.val:
        r.. F..
      p1 = p1.next
      p2 = p2.next
    r.. T..
