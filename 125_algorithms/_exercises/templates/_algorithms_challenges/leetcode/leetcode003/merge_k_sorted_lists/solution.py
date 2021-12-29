_______ heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    ___ mergeKLists(self, lists):
        __ n.. lists:
            r.. N..
        n = l..(lists)
        __ n __ 1:
            r.. lists[0]
        mid = n / 2
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])
        r.. self.merge(l1, l2)

    ___ merge(self, l1, l2):
        res = N..
        end = N..
        cur = N..
        __ l1 __ N..
            r.. l2
        __ l2 __ N..
            r.. l1
        while l1 __ n.. N.. and l2 __ n.. N..
            __ l1.val < l2.val:
                cur = l1
                l1 = l1.next
            ____:
                cur = l2
                l2 = l2.next
            __ res __ N..
                res = cur
                end = cur
            ____:
                end.next = cur
                end = end.next
        __ l1 __ n.. N..
            end.next = l1
        __ l2 __ n.. N..
            end.next = l2
        r.. res

    ___ mergeKLists2(self, lists):
        # Create a priority queue
        h    # list
        res = N..
        end = N..
        ___ l __ lists:
            __ l __ n.. N..
                heapq.heappush(h, (l.val, l))
        while h:
            l = heapq.heappop(h)[1]
            __ res __ N..
                res = l
                end = l
            ____:
                end.next = l
                end = end.next
            __ l.next __ n.. N..
                l = l.next
                heapq.heappush(h, (l.val, l))
        r.. res
