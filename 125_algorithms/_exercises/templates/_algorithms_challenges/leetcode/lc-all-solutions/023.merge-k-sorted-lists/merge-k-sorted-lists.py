# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None
______ heapq

# overwrite the comparison function, so the node can be comparable
ListNode.__lt__ = lambda x, y: (x.val < y.val)

class Solution(object
  ___ mergeKLists(self, lists
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap = []
    p = dummy = ListNode(-1)
    for i in range(0, le.(lists)):
      node = lists[i]
      __ not node:
        continue
      heapq.heappush(heap, node)

    w___ heap:
      value, node = heapq.heappop(heap)
      p.next = node
      p = p.next
      __ node.next:
        node = node.next
        heapq.heappush(heap, node)
    r_ dummy.next
