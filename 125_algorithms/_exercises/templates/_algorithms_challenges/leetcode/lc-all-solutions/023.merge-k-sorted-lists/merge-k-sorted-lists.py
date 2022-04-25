# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
_______ h__

# overwrite the comparison function, so the node can be comparable
ListNode.-l l.... x, y: (x.val < y.val)

c_ Solution(o..
  ___ mergeKLists  lists
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap    # list
    p dummy ListNode(-1)
    ___ i __ r..(0, l..(lists:
      node lists[i]
      __ n.. node:
        _____
      h__.heappush(heap, node)

    w.... heap:
      value, node h__.heappop(heap)
      p.next node
      p p.next
      __ node.next:
        node node.next
        h__.heappush(heap, node)
    r.. dummy.next
