c_ Solution(object):
  ___ insertionSortList(self, head):
    p = dummy = ListNode(0)
    cur = dummy.next = head
    w.... cur a.. cur.next:
      val = cur.next.val
      __ cur.val < val:
        cur = cur.next
        continue
      __ p.next.val > val:
        p = dummy
      w.... p.next.val < val:
        p = p.next
      new = cur.next
      cur.next = new.next
      new.next = p.next
      p.next = new
    r.. dummy.next
