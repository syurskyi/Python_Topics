# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


c_ Solution o..
    ___ plusOne  head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ? 0
        dummy.next = head
        place_stop, tail = dummy, dummy
        # find the tail
        w.. tail.next is not N..:
            tail = tail.next
            __ tail.val != 9:
                place_stop = tail
        __ tail.val != 9:
            # done
            tail.val += 1
        ____
            # not yet
            place_stop.val += 1
            place_stop = place_stop.next
            # set all node behind this place to zero
            w.. place_stop is not N..:
                place_stop.val = 0
                place_stop = place_stop.next
        __ dummy.val __ 0:
            r_ dummy.next
        r_ dummy
