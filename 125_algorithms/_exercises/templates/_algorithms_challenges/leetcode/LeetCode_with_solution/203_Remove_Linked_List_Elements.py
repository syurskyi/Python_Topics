# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    ___ removeElements  head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # add a extra head for removing head
        prehead = ListNode(-1)
        prehead.next = head
        last, pos = prehead, head
        w.. pos is not N..:
            __ pos.val __ val:
                last.next = pos.next
            ____
                last = pos
            pos = pos.next
        r_ prehead.next

