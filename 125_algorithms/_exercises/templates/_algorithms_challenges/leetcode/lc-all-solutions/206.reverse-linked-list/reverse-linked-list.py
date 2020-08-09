# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
  ___ reverseList(self, root
    __ not root or not root.next:
      r_ root

    ret = self.reverseList(root.next)
    root.next.next = root
    root.next = None
    r_ ret

  ___ _reverseList(self, head
    pre = None
    cur = head
    w___ cur:
      tmp = cur.next
      cur.next = pre
      pre = cur
      cur = tmp
    r_ pre

  # iteratively as queue head inserting
  ___ __reverseList(self, head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dHead = dummy = ListNode(-1)
    p = head
    w___ p:
      tmp = dummy.next
      dummy.next = p
      p = p.next
      dummy.next.next = tmp
    r_ dHead.next

  # easily leads to a circle. Remove current node's next after recursive call.
  ___ ___reverseList(self, head
    self.newHead = None

    ___ rec(head
      __ not head:
        r_ head
      p = rec(head.next)
      head.next = None
      __ p:
        p.next = head
      ____
        self.newHead = head
      r_ head

    rec(head)
    r_ self.newHead
