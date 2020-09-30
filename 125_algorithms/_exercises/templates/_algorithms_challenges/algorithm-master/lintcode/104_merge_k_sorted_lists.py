"""
Definition of ListNode
class ListNode(object
    ___ __init__(self, val, next=None
        self.val = val
        self.next = next
"""
______ heapq


class Solution:
    ___ mergeKLists(self, lists
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        __ not lists:
            r_

        dummy = tail = ListNode(-1)
        heap =   # list

        ___ i __ range(le.(lists)):
            __ not lists[i]:
                continue

            heapq.heappush(heap, (lists[i].val, i))

        w___ heap:
            val, i = heapq.heappop(heap)

            tail.next = ListNode(val)
            tail = tail.next

            __ lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))

        r_ dummy.next
