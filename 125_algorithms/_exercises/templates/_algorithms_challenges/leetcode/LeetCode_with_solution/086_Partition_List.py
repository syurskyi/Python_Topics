# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    ___ partition  head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        __ head is N..:
            r_ N..
        less = lesshead = N..
        last = pos = head
        w.. pos is not N..:
            __ pos.val < x:
                __ lesshead is N..:
                    lesshead = pos
                ____
                    less.next = pos
                less = pos
                __ head __ pos:
                    last = head = pos.next
                ____
                    last.next = pos.next
            ____
                last = pos
            pos = pos.next
        __ lesshead is not N..:
            less.next = head
        ____
            lesshead = head
        r_ lesshead