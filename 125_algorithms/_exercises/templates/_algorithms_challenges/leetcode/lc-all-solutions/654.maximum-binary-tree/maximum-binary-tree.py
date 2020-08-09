# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  # recursion
  ___ _constructMaximumBinaryTree(self, nums
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    __ nums:
      pos = nums.index(max(nums))
      root = TreeNode(nums[pos])
      root.left = self.constructMaximumBinaryTree(nums[:pos])
      root.right = self.constructMaximumBinaryTree(nums[pos + 1:])
      r_ root

  # decreasing stack
  ___ constructMaximumBinaryTree(self, nums
    stack = []
    for num in nums:
      root = TreeNode(num)
      w___ stack and stack[-1].val < num:
        root.left = stack.pop()
      __ stack:
        stack[-1].right = root
      stack.append(root)
    r_ stack and stack[0]
