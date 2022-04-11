"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
__author__ 'Daniel'


# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x
        val x
        next N..


c_ Solution(o..
    ___ oddEvenList  head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head:
            r..

        ptr head  # end of odd position
        pre head  # don't move the first
        cnt 1
        w.... pre a.. pre.next:
            cur pre.next
            cnt += 1
            __ cnt % 2 __ 0:
                pre pre.next
            ____
                start ptr.next
                nxt cur.next

                ptr.next cur
                cur.next start
                pre.next nxt

                ptr ptr.next

        r.. head

    ___ oddEvenListError  head
        """
        Wrongly move by node value
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head:
            r..

        ptr head  # end of first parity
        parity ptr.val % 2

        pre head
        w.... pre a.. pre.next:
            cur pre.next
            __ cur.val % 2 != parity:
                pre pre.next
            ____
                start ptr.next
                nxt cur.next

                ptr.next cur
                cur.next start
                pre.next nxt

                ptr ptr.next

        r.. head
