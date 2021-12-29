# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
_______ random


class Solution(object):

  ___ __init__(self, head):
    """
    @param head The linked list's head.
    Note that the head is guaranteed to be not null, so it contains at least one node.
    :type head: ListNode
    """
    self.head = head

  ___ getRandom(self):
    """
    Returns a random node's value.
    :rtype: int
    """
    ans = self.head.val
    head = self.head
    idx = 1
    w.... head:
      __ random.randrange(1, idx + 1) __ idx:
        ans = head.val
      head = head.next
      idx += 1
    r.. ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
