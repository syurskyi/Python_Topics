# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    ___ partition(self, head, x):
        __ head __ N..
            r.. head
        large = N..
        large_end = N..
        res = N..
        res_end = N..
        w.... head __ n.. N..
            next_node = head.next
            __ head.val >= x:
                __ large __ N..
                    large = head
                    large_end = large
                ____:
                    large_end.next = head
                    large_end = large_end.next
            ____:
                __ res __ N..
                    res = head
                    res_end = res
                ____:
                    res_end.next = head
                    res_end = res_end.next
            head = next_node
        __ large_end __ n.. N..
            large_end.next = N..
        __ res __ n.. N..
            res_end.next = large
        ____:
            res = large
        r.. res
