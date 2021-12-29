# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ___ sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        __ not nums:
            return

        i = len(nums) // 2
        node = TreeNode(nums[i])
        node.left = self.sortedArrayToBST(nums[:i])
        node.right = self.sortedArrayToBST(nums[i + 1:])

        return node
