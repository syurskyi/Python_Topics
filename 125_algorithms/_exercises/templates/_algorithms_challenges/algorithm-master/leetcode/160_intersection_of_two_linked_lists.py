# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


c_ Solution(object):
    ___ getIntersectionNode(self, A, B):
        """
        :type A, B: ListNode
        :rtype: ListNode
        """
        __ n.. A o. n.. B:
            r..

        X, Y = A, B

        w.... X a.. Y:
            X = X.next
            Y = Y.next

        w.... X:
            X = X.next
            A = A.next

        w.... Y:
            Y = Y.next
            B = B.next

        w.... A __ n.. B:
            A = A.next
            B = B.next

        r.. A
