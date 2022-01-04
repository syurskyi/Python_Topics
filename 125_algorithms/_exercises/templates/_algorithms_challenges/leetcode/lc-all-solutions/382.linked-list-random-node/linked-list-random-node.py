# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
_______ r__


c_ Solution(object):

  ___ - , head):
    """
    @param head The linked list's head.
    Note that the head is guaranteed to be not null, so it contains at least one node.
    :type head: ListNode
    """
    head = head

  ___ getRandom
    """
    Returns a random node's value.
    :rtype: int
    """
    ans = head.val
    head = head
    idx = 1
    w.... head:
      __ r__.randrange(1, idx + 1) __ idx:
        ans = head.val
      head = head.next
      idx += 1
    r.. ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
