# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    # https://leetcode.com/articles/intersection-two-linked-lists/
    ___ getIntersectionNode  headA, headB
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # two points
        __ n.. headA or n.. headB:
            r_ N..
        a, b = headA, headB
        ans = N..
        w.. a or b:
            __ n.. a:
                a = headB
            __ n.. b:
                b = headA
            __ a __ b and n.. ans:
                ans = a
            a, b = a.next, b.next
        r_ ans
