"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None

    ___ __repr__(self
        r_ repr(self.val)

class Solution:
    ___ rotateRight(self, head, k
        """
        Linked list
        Assume k is legal

        :param head: ListNode
        :param k: an integer
        :return: ListNode
        """
        __ not head:
            r_ None


        dummy = ListNode(0)
        dummy.next = head

        # find length
        length = 0
        pre = dummy
        w___ pre.next:
            length += 1
            pre = pre.next
        # find the last one
        last = pre

        # normalize, since possible k > length
        k = k%length  # k is length in nature

        # find breaking point
        count = 0
        pre = dummy
        w___ count<length-k:  # you will appreciate python's half open range and 0-based index k
            count += 1
            pre = pre.next

        # then do the manipulate in one group of operations (no loop)
        __ k!=0: # avoid cyclic link
            pre.next, dummy.next, last.next = None, pre.next, dummy.next

        r_ dummy.next

__ __name____"__main__":
    length = 1
    lst = [ListNode(i+1) ___ i __ xrange(length)]
    ___ i __ range(length-1
        lst[i].next = lst[i+1]
    Solution().rotateRight(lst[0], 1)
