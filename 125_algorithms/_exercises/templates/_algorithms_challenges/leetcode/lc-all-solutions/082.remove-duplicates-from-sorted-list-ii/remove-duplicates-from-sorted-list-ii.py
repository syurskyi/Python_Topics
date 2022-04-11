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
    dummy ListNode(-1)
    dummy.next head
    p dummy
    w.... p.next:
      __ p.next.next a.. p.next.val __ p.next.next.val:
        z p.next
        w.... z a.. z.next a.. z.val __ z.next.val:
          z z.next
        p.next z.next
      ____
        p p.next
    r.. dummy.next
