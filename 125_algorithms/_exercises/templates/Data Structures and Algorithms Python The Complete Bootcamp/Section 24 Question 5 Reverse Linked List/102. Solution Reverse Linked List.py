# Definition for singly-linked list.
class ListNode:
    ___  -   val=0, next=N..):
        val = val
        next = next


class Solution:
    ___ reverseList  head):
        pre = N..
        cur = head
        suc = N..

        w__ cur:
            suc = cur.next
            cur.next = pre
            pre = cur
            cur = suc

        r_ pre