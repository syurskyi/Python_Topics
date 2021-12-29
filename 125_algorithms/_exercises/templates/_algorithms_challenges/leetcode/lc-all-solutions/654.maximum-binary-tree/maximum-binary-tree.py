# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  # recursion
  ___ _constructMaximumBinaryTree(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    __ nums:
      pos = nums.index(max(nums))
      root = TreeNode(nums[pos])
      root.left = self.constructMaximumBinaryTree(nums[:pos])
      root.right = self.constructMaximumBinaryTree(nums[pos + 1:])
      r.. root

  # decreasing stack
  ___ constructMaximumBinaryTree(self, nums):
    stack    # list
    ___ num __ nums:
      root = TreeNode(num)
      while stack and stack[-1].val < num:
        root.left = stack.pop()
      __ stack:
        stack[-1].right = root
      stack.a..(root)
    r.. stack and stack[0]
