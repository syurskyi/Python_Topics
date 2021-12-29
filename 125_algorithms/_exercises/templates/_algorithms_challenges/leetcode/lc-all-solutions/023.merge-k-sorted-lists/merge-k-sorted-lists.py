# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
_______ heapq

# overwrite the comparison function, so the node can be comparable
ListNode.__lt__ = l.... x, y: (x.val < y.val)

class Solution(object):
  ___ mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap    # list
    p = dummy = ListNode(-1)
    ___ i __ r..(0, l..(lists)):
      node = lists[i]
      __ n.. node:
        continue
      heapq.heappush(heap, node)

    while heap:
      value, node = heapq.heappop(heap)
      p.next = node
      p = p.next
      __ node.next:
        node = node.next
        heapq.heappush(heap, node)
    r.. dummy.next
