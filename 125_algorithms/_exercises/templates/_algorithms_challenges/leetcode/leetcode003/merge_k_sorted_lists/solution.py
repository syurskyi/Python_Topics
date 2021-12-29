import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    ___ mergeKLists(self, lists):
        __ not lists:
            return None
        n = len(lists)
        __ n == 1:
            return lists[0]
        mid = n / 2
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])
        return self.merge(l1, l2)

    ___ merge(self, l1, l2):
        res = None
        end = None
        cur = None
        __ l1 is None:
            return l2
        __ l2 is None:
            return l1
        while l1 is not None and l2 is not None:
            __ l1.val < l2.val:
                cur = l1
                l1 = l1.next
            else:
                cur = l2
                l2 = l2.next
            __ res is None:
                res = cur
                end = cur
            else:
                end.next = cur
                end = end.next
        __ l1 is not None:
            end.next = l1
        __ l2 is not None:
            end.next = l2
        return res

    ___ mergeKLists2(self, lists):
        # Create a priority queue
        h = []
        res = None
        end = None
        for l in lists:
            __ l is not None:
                heapq.heappush(h, (l.val, l))
        while h:
            l = heapq.heappop(h)[1]
            __ res is None:
                res = l
                end = l
            else:
                end.next = l
                end = end.next
            __ l.next is not None:
                l = l.next
                heapq.heappush(h, (l.val, l))
        return res
