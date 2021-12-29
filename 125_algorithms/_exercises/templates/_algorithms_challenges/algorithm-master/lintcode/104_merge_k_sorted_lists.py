"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq


class Solution:
    ___ mergeKLists(self, lists):
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        __ not lists:
            return

        dummy = tail = ListNode(-1)
        heap = []

        for i in range(len(lists)):
            __ not lists[i]:
                continue

            heapq.heappush(heap, (lists[i].val, i))

        while heap:
            val, i = heapq.heappop(heap)

            tail.next = ListNode(val)
            tail = tail.next

            __ lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next
