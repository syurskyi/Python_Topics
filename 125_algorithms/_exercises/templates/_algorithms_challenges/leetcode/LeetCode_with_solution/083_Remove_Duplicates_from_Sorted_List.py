# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    # def deleteDuplicates(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #     temp = ListNode(2147483647)
    #     temp.next = head
    #     pos = head
    #     head = temp
    #     last = head
    #     while pos is not None:
    #         if last.val == pos.val:
    #             last.next = pos.next
    #         else:
    #             last = pos
    #         pos = pos.next
    #     return head.next

    ___ deleteDuplicates  head
        __ head is N..:
            r_ N..
        pos = head
        w.. pos is n.. N.. and pos.next is n.. N..:
            __ pos.val __ pos.next.val:
                pos.next = pos.next.next
            ____
                pos = pos.next
        r_ head
