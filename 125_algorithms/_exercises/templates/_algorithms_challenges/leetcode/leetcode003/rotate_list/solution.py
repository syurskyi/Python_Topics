# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    ___ rotateRight  head, k
        __ head __ N..
            r.. N..
        n = 0
        h = head
        w.... head __ n.. N..
            n += 1
            head = head.next
        k = k % n
        __ k __ 0:
            r.. h
        res = h  # Head of result
        prev = h  # Previous node of result
        i = 0
        w.... res __ n.. N..
            __ i __ n - k:
                _____
            prev = res
            res = res.next
            i += 1
        end = res
        w.... end.next __ n.. N..
            end = end.next
        end.next = h
        prev.next = N..
        r.. res
