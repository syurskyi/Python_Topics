# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None


class Solution(object
    ___ getIntersectionNode(self, A, B
        """
        :type A, B: ListNode
        :rtype: ListNode
        """
        __ not A or not B:
            r_

        X, Y = A, B

        w___ X and Y:
            X = X.next
            Y = Y.next

        w___ X:
            X = X.next
            A = A.next

        w___ Y:
            Y = Y.next
            B = B.next

        w___ A is not B:
            A = A.next
            B = B.next

        r_ A
