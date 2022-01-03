# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

c_ Solution(object):
  ___ copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    p = head
    w.... p:
      copy = RandomListNode(p.label)
      copy.next = p.next
      p.next = copy
      p = copy.next

    p = head
    w.... p:
      p.next.random = p.random a.. p.random.next
      p = p.next.next

    p = head
    copy = chead = head a.. head.next
    w.... p:
      p.next = p = copy.next
      copy.next = copy = p a.. p.next
    r.. chead
