# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
c_ Solution o..
    ___ mergeTwoLists  l1, l2
        # dummy head
        pos = dummyHead = ListNode(-1)
        w.. l1 is n.. N.. a.. l2 is n.. N..:
            __ l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            ____
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        # merge residual l1
        __ l1 is n.. N..:
            pos.next = l1
        # merge residual l2
        __ l2 is n.. N..:
            pos.next = l2
        r_ dummyHead.next


    # def mergeTwoLists(self, l1, l2):
    #     # recursive
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1
    #     if l1.val <= l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

