# Reverse Linked List II
# Question: Reverse a linked list from position m to n. Do it in-place and in one-pass.
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# Return 1->4->3->2->5->NULL.
# Note: Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
# Solutions:


c_ ListNode object:
    ___  - , x:
        val _ x
        next _ N..

    ___ to_list
        r_ [val] + next.to_list  __ next ____ [val]


c_ Solution object:
    ___ reverseBetween , head, m, n:
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy _ ListNode -1
        dummy.next _ head
        node _ dummy
        ___ __ __ ra.. m - 1:
            node _ node.next
        prev _ node.next
        curr _ prev.next
        ___ __ __ ra.. n - m:
            next _ curr.next
            curr.next _ prev
            prev _ curr
            curr _ next
        node.next.next _ curr
        node.next _ prev
        r_ dummy.next


__  -n __ _____
    n1 _ ListNode 1
    n2 _ ListNode 2
    n3 _ ListNode 3
    n4 _ ListNode 4
    n5 _ ListNode 5
    n1.next _ n2
    n2.next _ n3
    n3.next _ n4
    n4.next _ n5
    r _ Solution .reverseBetween n1, 2, 4
    print   r.to_list  