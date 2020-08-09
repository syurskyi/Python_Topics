# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ isPalindrome(self, head
    """
    :type head: ListNode
    :rtype: bool
    """

    ___ reverseList(root
      pre = None
      cur = root
      w___ cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      r_ pre

    slow = fast = head
    w___ fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    newHead = reverseList(slow)
    p1 = head
    p2 = newHead
    w___ p1 and p2:
      __ p1.val != p2.val:
        r_ False
      p1 = p1.next
      p2 = p2.next
    r_ True
