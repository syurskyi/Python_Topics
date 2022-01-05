# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..):
  ___ reverseList  root):
    __ n.. root o. n.. root.next:
      r.. root

    ret = reverseList(root.next)
    root.next.next = root
    root.next = N..
    r.. ret

  ___ _reverseList  head):
    pre = N..
    cur = head
    w.... cur:
      tmp = cur.next
      cur.next = pre
      pre = cur
      cur = tmp
    r.. pre

  # iteratively as queue head inserting
  ___ __reverseList  head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dHead = dummy = ListNode(-1)
    p = head
    w.... p:
      tmp = dummy.next
      dummy.next = p
      p = p.next
      dummy.next.next = tmp
    r.. dHead.next

  # easily leads to a circle. Remove current node's next after recursive call.
  ___ ___reverseList  head):
    newHead = N..

    ___ rec(head):
      __ n.. head:
        r.. head
      p = rec(head.next)
      head.next = N..
      __ p:
        p.next = head
      ____:
        newHead = head
      r.. head

    rec(head)
    r.. newHead
