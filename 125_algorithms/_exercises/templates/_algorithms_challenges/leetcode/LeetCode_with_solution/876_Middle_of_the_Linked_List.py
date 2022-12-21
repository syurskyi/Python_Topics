# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    # def middleNode(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     res = []
    #     while head:
    #         res.append(head)
    #         head = head.next
    #     return res[len(res) / 2]

    ___ middleNode  head
        # Fast point is 2 times faster than slow point
        fast = slow = head
        w.. fast a.. fast.next:
            slow = slow.next
            fast = fast.next.next
        r_ slow
