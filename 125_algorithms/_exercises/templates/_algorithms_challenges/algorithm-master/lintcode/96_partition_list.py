"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


c_ Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    ___ partition  head, x
        __ n.. head:
            r..

        left_dummy = left_tail = ListNode(-1)
        right_dummy = right_tail = ListNode(-1)

        w.... head:
            node = ListNode(head.val)
            __ head.val < x:
                left_tail.next = node
                left_tail = node
            ____
                right_tail.next = node
                right_tail = node
            head = head.next

        left_tail.next = right_dummy.next
        r.. left_dummy.next
