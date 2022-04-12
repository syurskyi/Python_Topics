"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
_______ h__


c_ Solution:
    ___ mergeKLists  lists
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        __ n.. lists:
            r..

        dummy tail ListNode(-1)
        heap    # list

        ___ i __ r..(l..(lists:
            __ n.. lists[i]:
                _____

            h__.heappush(heap, (lists[i].val, i

        w.... heap:
            val, i h__.heappop(heap)

            tail.next ListNode(val)
            tail tail.next

            __ lists[i].next:
                lists[i] lists[i].next
                h__.heappush(heap, (lists[i].val, i

        r.. dummy.next
