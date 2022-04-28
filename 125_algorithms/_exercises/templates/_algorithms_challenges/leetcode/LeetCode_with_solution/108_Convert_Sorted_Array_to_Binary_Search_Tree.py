# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def sortedArrayToBST(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: TreeNode
    #     """
    #     # Recursion with slicing
    #     if not nums:
    #         return None
    #     mid = len(nums) / 2
    #     root = TreeNode(nums[mid])
    #     root.left = self.sortedArrayToBST(nums[:mid])
    #     root.right = self.sortedArrayToBST(nums[mid + 1:])
    #     return root

    ___ sortedArrayToBST  nums):
        # Recursion with index
        r_ getHelper(nums, 0, l.. nums) - 1)

    ___ getHelper  nums, start, end):
        __ start > end:
            r_ N..
        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        node.left = getHelper(nums, start, mid - 1)
        node.right = getHelper(nums, mid + 1, end)
        r_ node