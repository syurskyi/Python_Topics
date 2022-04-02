# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ removeNthFromEnd  head, n
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    fast = slow = dummy

    w.... n a.. fast:
      fast = fast.next
      n -= 1

    w.... fast.next a.. slow.next:
      fast = fast.next
      slow = slow.next

    slow.next = slow.next.next
    r.. dummy.next
