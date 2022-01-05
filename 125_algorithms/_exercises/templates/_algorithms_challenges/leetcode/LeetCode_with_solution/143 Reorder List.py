"""
Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x):
        val = x
        next = N..

    ___ __repr__
        r.. repr(val)

c_ Solution:
    ___ reorderList_TLE  head):
        """
        :param head: ListNode
        :return: nothing
        """
        dummy_head = ListNode(0)
        dummy_head.next = head

        pre_cur = dummy_head
        w....(pre_cur a.. pre_cur.next):
            # find last
            pre_last = pre_cur.next
            __ pre_last.next __ N..
                r..
            w....(pre_last.next.next):
                pre_last = pre_last.next

            last = pre_last.next

            # shift
            cur = pre_cur.next
            cur_next = cur.next
            __ cur_next!= last a.. cur!= last:
                cur.next = last
                last.next = cur_next
                # fix last
                pre_last.next = N..

            __ cur_next a.. cur_next.next__last:
                cur_next.next = N..


            pre_cur = pre_cur.next.next

    ___ reorderList_array  head):
        """
        Not in place

        relies on additional data structure 
        """
        lst    # list
        cur = head
        w....(cur):
            lst.a..(cur)
            cur = cur.next

        lst1 = lst[:l..(lst)/2]
        lst2 = lst[l..(lst)/2:]
        lst2.reverse()

        lst    # list
        ___ i __ r..(l..(lst2)):
            ___
                lst.a..(lst1[i])
            ______ IndexError:
                p..
            lst.a..(lst2[i])

        ___ i __ r..(l..(lst)):
            ___
                lst[i].next = lst[i+1]
            ______ IndexError:
                lst[i].next = N..

    ___ reorderList  head):
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
        w.... fast_pre.next a.. fast_pre.next.next:
            fast_pre = fast_pre.next
            fast_pre = fast_pre.next
            slow_pre = slow_pre.next

        # reverse the 2nd half, pre & cur
        mid = slow_pre.next

        pre = mid
        cur = pre.next
        w.... pre a.. cur:  # problem reduction
            cur.next, pre, cur = pre, cur, cur.next
        mid.next = N..

        # merge
        last = pre
        cur = dummy.next
        w.... cur!=mid a.. last!=mid:
            cur.next, last.next, last, cur = last, cur.next, last.next, cur.next








__ _____ __ ____
    length = 2
    lst = [ListNode(i+1) ___ i __ r..(length)]
    ___ i __ r..(length-1):
        lst[i].next = lst[i+1]

    Solution().reorderList(lst[0])

    cur = lst[0]
    w....(cur):
        print cur.val
        cur = cur.next
