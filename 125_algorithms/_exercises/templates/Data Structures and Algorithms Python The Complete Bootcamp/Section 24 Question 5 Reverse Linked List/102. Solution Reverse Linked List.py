# Definition for singly-linked list.
c_ ListNode:
    ___  -   val0, nextN..):
        val  val
        next  next


c_ Solution:
    ___ reverseList  head):
        pre  N..
        cur  head
        suc  N..

        w__ cur:
            suc  cur.next
            cur.next  pre
            pre  cur
            cur  suc

        r_ pre