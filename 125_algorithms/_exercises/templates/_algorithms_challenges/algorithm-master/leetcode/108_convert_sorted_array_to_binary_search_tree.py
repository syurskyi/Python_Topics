# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution:
    ___ sortedArrayToBST  nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        __ n.. nums:
            r..

        i = l..(nums) // 2
        node = TreeNode(nums[i])
        node.left = sortedArrayToBST(nums[:i])
        node.right = sortedArrayToBST(nums[i + 1:])

        r.. node
