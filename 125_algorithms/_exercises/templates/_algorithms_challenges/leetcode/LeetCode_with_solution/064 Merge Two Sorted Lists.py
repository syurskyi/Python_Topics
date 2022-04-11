"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.
"""
__author__ 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x
        val x
        next N..

    ___  -r
        r.. r.. (val)

    ___ -s
        r.. "%d, %s"%(val, next)

c_ Solution:
    ___ mergeTwoLists  l1, l2
        """
        Linked List
        assuming ascending order
        :param l1: ListNode
        :param l2: ListNode
        :return:
        """
        dummy ListNode(0)
        dummy.next l1

        pre dummy
        the_other l2
        w.... pre a.. pre.next:
            cur pre.next
            __ the_other a.. cur.val>the_other.val:
                # insert
                temp the_other.next
                pre.next, the_other.next the_other, cur

                the_other temp  # advance the_other
            pre pre.next


        # dangling list
        __ the_other:
            pre.next the_other  # appending

        r.. dummy.next

__ _____ __ ____
    length 10
    list1 [ListNode(2*i) ___ i __ x..(length)]
    list2 [ListNode(2*i+1) ___ i __ x..(length)]
    ___ i __ x..(length-1
        list1[i].next list1[i+1]
        list2[i].next list2[i+1]

    lst Solution().mergeTwoLists(list1[0], list2[0])
    print lst
