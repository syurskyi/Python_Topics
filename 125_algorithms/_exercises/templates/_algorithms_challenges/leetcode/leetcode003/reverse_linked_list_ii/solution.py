# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    ___ reverseBetween  head, m, n
        i = 1
        res = head  # Start of the beginning part
        res_end = head  # End of the beginning part
        rev = N..  # Start of reversed part
        rev_end = N..  # End of reversed part
        w.... head __ n.. N..
            next_node = head.next
            __ i < m:
                res_end = head
            ____ i >_ m a.. i <_ n:
                head.next = rev
                rev = head
                __ i __ m:
                    rev_end = head
            ____  # i > n
                _____
            head = next_node
            i += 1
        # No beginning part
        __ m __ 1:
            res = rev
            res_end = rev_end
        ____
            res_end.next = rev
        rev_end.next = head
        r.. res
