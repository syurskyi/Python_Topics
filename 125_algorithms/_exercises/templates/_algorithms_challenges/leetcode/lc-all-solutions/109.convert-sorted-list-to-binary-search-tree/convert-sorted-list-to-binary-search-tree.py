# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ sortedListToBST  head
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    __ head:
      pre  N..
      slow  fast  head
      w.... fast a.. fast.next:
        pre  slow
        slow  slow.next
        fast  fast.next.next
      root  TreeNode(slow.val)
      __ pre:
        pre.next  N..
        root.left sortedListToBST(head)
      root.right sortedListToBST(slow.next)
      r.. root
