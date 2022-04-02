# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
  ___ deleteDuplicates  head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(N..)
    dummy.next = head
    p = dummy

    w.... p a.. p.next:
      __ p.val __ p.next.val:
        p.next = p.next.next
      ____:
        p = p.next
    r.. dummy.next
