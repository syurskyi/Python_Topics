"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
_______ heapq


c_ Solution:
    ___ mergeKLists(self, lists):
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        __ n.. lists:
            r..

        dummy = tail = ListNode(-1)
        heap    # list

        ___ i __ r..(l..(lists)):
            __ n.. lists[i]:
                _____

            heapq.heappush(heap, (lists[i].val, i))

        w.... heap:
            val, i = heapq.heappop(heap)

            tail.next = ListNode(val)
            tail = tail.next

            __ lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))

        r.. dummy.next
