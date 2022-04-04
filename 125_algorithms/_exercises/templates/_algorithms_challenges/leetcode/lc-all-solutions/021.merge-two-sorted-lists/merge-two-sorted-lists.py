# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ mergeTwoLists  l1, l2
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = dummy = ListNode(-1)
    w.... l1 a.. l2:
      __ l1.val < l2.val:
        head.next = l1
        l1 = l1.next
      ____
        head.next = l2
        l2 = l2.next
      head = head.next
    __ l1:
      head.next = l1
    __ l2:
      head.next = l2
    r.. dummy.next
