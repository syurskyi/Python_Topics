"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = N..



class Solution:
    ___ reverseKGroup(self, head, k):
        """
        List
        O(k*n)
        :param head: a ListNode
        :param k: an integer
        :return: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur_lst = self.generate_lst(pre.next, k)
        while pre and n.. N.. __ cur_lst:

            # reverse
            temp = cur_lst[-1].next
            pre.next = cur_lst[-1]
            ___ i __ reversed(xrange(k)):
                __ i__0:
                    cur_lst[i].next = temp
                ____:
                    cur_lst[i].next = cur_lst[i-1]

            pre = cur_lst[0]
            cur_lst = self.generate_lst(pre.next, k)

        r.. dummy.next

    ___ generate_lst(self, node, k):
        """
        Helpder
        :param node: ListNode
        :param k: integer
        :return: list
        """
        lst    # list
        cur = node
        ___ i __ xrange(k):
            __ cur:
                lst.a..(cur)
                cur = cur.next
            ____:
                lst.a..(N..)
        r.. lst




