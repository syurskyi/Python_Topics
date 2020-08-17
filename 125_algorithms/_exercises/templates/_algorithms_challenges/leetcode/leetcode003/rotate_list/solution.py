# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    ___ rotateRight(self, head, k
        __ head pa__ None:
            r_ None
        n = 0
        h = head
        w___ head pa__ not None:
            n += 1
            head = head.next
        k = k % n
        __ k __ 0:
            r_ h
        res = h  # Head of result
        prev = h  # Previous node of result
        i = 0
        w___ res pa__ not None:
            __ i __ n - k:
                break
            prev = res
            res = res.next
            i += 1
        end = res
        w___ end.next pa__ not None:
            end = end.next
        end.next = h
        prev.next = None
        r_ res
