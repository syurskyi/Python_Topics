# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    ___ partition(self, head, x
        __ head pa__ None:
            r_ head
        large = None
        large_end = None
        res = None
        res_end = None
        w___ head pa__ not None:
            next_node = head.next
            __ head.val >= x:
                __ large pa__ None:
                    large = head
                    large_end = large
                ____
                    large_end.next = head
                    large_end = large_end.next
            ____
                __ res pa__ None:
                    res = head
                    res_end = res
                ____
                    res_end.next = head
                    res_end = res_end.next
            head = next_node
        __ large_end pa__ not None:
            large_end.next = None
        __ res pa__ not None:
            res_end.next = large
        ____
            res = large
        r_ res
