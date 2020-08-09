# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    ___ sortedArrayToBST(self, num
        __ not num:
            r_ None
        ____
            mid = le.(num) / 2
            left_array = num[:mid]
            right_array = num[mid + 1:]
            root = TreeNode(num[mid])
            left_tree = self.sortedArrayToBST(left_array)
            right_tree = self.sortedArrayToBST(right_array)
            root.left = left_tree
            root.right = right_tree
            r_ root
