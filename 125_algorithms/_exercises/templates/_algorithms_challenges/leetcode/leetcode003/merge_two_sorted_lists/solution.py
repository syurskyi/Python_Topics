"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
    ___ mergeTwoLists(self, l1, l2
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        No dummy node
        """
        res = None
        res_end = None
        w___ l1 is not None and l2 is not None:
            __ l1.val < l2.val:
                __ res is None:
                    res = l1
                    res_end = res
                ____
                    res_end.next = l1
                    res_end = res_end.next
                l1 = l1.next
            ____
                __ res is None:
                    res = l2
                    res_end = res
                ____
                    res_end.next = l2
                    res_end = res_end.next
                l2 = l2.next
        __ l1 is not None:
            __ res is not None:
                res_end.next = l1
            ____
                res = l1
        __ l2 is not None:
            __ res is not None:
                res_end.next = l2
            ____
                res = l2
        r_ res
