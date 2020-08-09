# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ sortedListToBST(self, head
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    __ head:
      pre = None
      slow = fast = head
      w___ fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
      root = TreeNode(slow.val)
      __ pre:
        pre.next = None
        root.left = self.sortedListToBST(head)
      root.right = self.sortedListToBST(slow.next)
      r_ root
