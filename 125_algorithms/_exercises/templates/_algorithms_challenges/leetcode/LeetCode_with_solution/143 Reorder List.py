"""
Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = N..

    ___ __repr__(self):
        r.. repr(self.val)

class Solution:
    ___ reorderList_TLE(self, head):
        """
        :param head: ListNode
        :return: nothing
        """
        dummy_head = ListNode(0)
        dummy_head.next = head

        pre_cur = dummy_head
        while(pre_cur and pre_cur.next):
            # find last
            pre_last = pre_cur.next
            __ pre_last.next __ N..
                r..
            while(pre_last.next.next):
                pre_last = pre_last.next

            last = pre_last.next

            # shift
            cur = pre_cur.next
            cur_next = cur.next
            __ cur_next!= last and cur!= last:
                cur.next = last
                last.next = cur_next
                # fix last
                pre_last.next = N..

            __ cur_next and cur_next.next__last:
                cur_next.next = N..


            pre_cur = pre_cur.next.next

    ___ reorderList_array(self, head):
        """
        Not in place

        relies on additional data structure 
        """
        lst    # list
        cur = head
        while(cur):
            lst.a..(cur)
            cur = cur.next

        lst1 = lst[:l..(lst)/2]
        lst2 = lst[l..(lst)/2:]
        lst2.reverse()

        lst    # list
        ___ i __ r..(l..(lst2)):
            try:
                lst.a..(lst1[i])
            except IndexError:
                pass
            lst.a..(lst2[i])

        ___ i __ r..(l..(lst)):
            try:
                lst[i].next = lst[i+1]
            except IndexError:
                lst[i].next = N..

    ___ reorderList(self, head):
        """
        Algorithm:
        1. find the mid point
        2. reverse the 2nd half
        3. merge the 1st half and 2nd half
        :param head: ListNode
        :return: nothing
        """
        __ n.. head:
            r..
        dummy = ListNode(0)
        dummy.next = head

        # find the mid point
        slow_pre = dummy
        fast_pre = dummy
        while fast_pre.next and fast_pre.next.next:
            fast_pre = fast_pre.next
            fast_pre = fast_pre.next
            slow_pre = slow_pre.next

        # reverse the 2nd half, pre & cur
        mid = slow_pre.next

        pre = mid
        cur = pre.next
        while pre and cur:  # problem reduction
            cur.next, pre, cur = pre, cur, cur.next
        mid.next = N..

        # merge
        last = pre
        cur = dummy.next
        while cur!=mid and last!=mid:
            cur.next, last.next, last, cur = last, cur.next, last.next, cur.next








__ __name____"__main__":
    length = 2
    lst = [ListNode(i+1) ___ i __ r..(length)]
    ___ i __ r..(length-1):
        lst[i].next = lst[i+1]

    Solution().reorderList(lst[0])

    cur = lst[0]
    while(cur):
        print cur.val
        cur = cur.next
