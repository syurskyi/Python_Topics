# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..):
  # recursion
  ___ _constructMaximumBinaryTree  nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    __ nums:
      pos = nums.index(m..(nums))
      root = TreeNode(nums[pos])
      root.left = constructMaximumBinaryTree(nums[:pos])
      root.right = constructMaximumBinaryTree(nums[pos + 1:])
      r.. root

  # decreasing stack
  ___ constructMaximumBinaryTree  nums):
    stack    # list
    ___ num __ nums:
      root = TreeNode(num)
      w.... stack a.. stack[-1].val < num:
        root.left = stack.pop()
      __ stack:
        stack[-1].right = root
      stack.a..(root)
    r.. stack a.. stack[0]
