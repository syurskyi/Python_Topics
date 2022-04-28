# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
c_ Solution o..
    ___ reverseKGroup  head, k):
        __ head is N..:
            r_ N..
        index = 0
        lead, last = 0, 0
        pos = head
        temp = ListNode(-1)
        temp.next = head
        head = temp
        start = head
        w.. pos is not N..:
            __ index % k __ k - 1:
                last = pos.next
                start = reverseList(start, last)
                pos = start
            pos = pos.next
            index += 1
        r_ head.next

    ___ reverseList  head, end):
        pos = head.next
        last = end
        next_start = pos
        w.. pos != end:
            head.next = pos
            last_pos = pos
            pos = pos.next
            last_pos.next = last
            last = last_pos
        r_ next_start


