# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     # Add max and check if reach max
    #     if head is None:
    #         return False
    #     count = 0
    #     max = 100000
    #     pos = head
    #     while pos is not None:
    #         count += 1
    #         pos = pos.next
    #         if count > max:
    #             return True
    #     return False

    # def hasCycle(self, head):
    #     # Hash or set
    #     dic = {}
    #     pos = head
    #     while pos is not None:
    #         try:
    #             dic[pos]
    #             return True
    #         except KeyError:
    #             dic[pos] = pos
    #         pos = pos.next
    #     return False

    ___ hasCycle  head):
        # Two points
        try:
            fast = head.next.next
            slow = head.next

            w.. fast != slow:
                fast = fast.next.next
                slow = slow.next

            r_ T..
        except:
            r_ F..