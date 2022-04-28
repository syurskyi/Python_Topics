# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    ___ detectCycle  head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Two points
        # https://discuss.leetcode.com/topic/2975/o-n-solution-by-using-two-pointers-without-change-anything
        try:
            fast = head.next.next
            slow = head.next

            w.. fast != slow:
                fast = fast.next.next
                slow = slow.next
        except:
            r_ N..
        slow = head
        w.. fast != slow:
            fast = fast.next
            slow = slow.next
        r_ fast

