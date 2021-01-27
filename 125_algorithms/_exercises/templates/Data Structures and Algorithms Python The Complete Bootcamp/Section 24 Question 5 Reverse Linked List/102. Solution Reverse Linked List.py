# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    ___ reverseList(self, head):
        pre = None
        cur = head
        suc = None

        w__ cur:
            suc = cur.next
            cur.next = pre
            pre = cur
            cur = suc

        r_ pre