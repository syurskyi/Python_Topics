"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
__author__ 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x
        val x
        next N..

    ___  -r
        r.. r.. (val)

c_ Solution:
    ___ rotateRight  head, k
        """
        Linked list
        Assume k is legal

        :param head: ListNode
        :param k: an integer
        :return: ListNode
        """
        __ n.. head:
            r.. N..


        dummy ListNode(0)
        dummy.next head

        # find length
        length 0
        pre dummy
        w.... pre.next:
            length += 1
            pre pre.next
        # find the last one
        last pre

        # normalize, since possible k > length
        k k%length  # k is length in nature

        # find breaking point
        count 0
        pre dummy
        w.... count<length-k:  # you will appreciate python's half open range and 0-based index k
            count += 1
            pre pre.next

        # then do the manipulate in one group of operations (no loop)
        __ k!_0: # avoid cyclic link
            pre.next, dummy.next, last.next N.., pre.next, dummy.next

        r.. dummy.next

__ _____ __ ____
    length 1
    lst [ListNode(i+1) ___ i __ x..(length)]
    ___ i __ r..(length-1
        lst[i].next lst[i+1]
    Solution().rotateRight(lst[0], 1)
