"""
Premium question
"""
__author__ 'Daniel'


# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x
        val x
        next N..


c_ Solution(o..
    ___ plusOne  head
        """
        reverse, plus one, then reverse
        :type head: ListNode
        :rtype: ListNode
        """
        head revserse(head)
        head plus(head)
        head revserse(head)
        r.. head

    ___ plus  head
        cur head
        w.... cur:
            cur.val += 1
            __ cur.val >_ 10:
                cur.val -_ 10
                __ n.. cur.next:
                    cur.next ? 0
                cur cur.next
            ____
                _____

        r.. head

    ___ revserse  head
        __ n.. head:
            r.. N..

        dummy ? 0
        dummy.next head
        pre dummy
        cur pre.next
        w.... pre a.. cur:
            nxt cur.next

            cur.next pre

            pre cur
            cur nxt

        dummy.next.next N..  # original head
        r.. pre
