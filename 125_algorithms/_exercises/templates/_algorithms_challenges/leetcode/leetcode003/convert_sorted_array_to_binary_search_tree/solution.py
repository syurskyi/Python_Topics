# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param num, a list of integers
    # @return a tree node
    ___ sortedArrayToBST  num):
        __ n.. num:
            r.. N..
        ____:
            mid = l..(num) / 2
            left_array = num[:mid]
            right_array = num[mid + 1:]
            root = TreeNode(num[mid])
            left_tree = sortedArrayToBST(left_array)
            right_tree = sortedArrayToBST(right_array)
            root.left = left_tree
            root.right = right_tree
            r.. root
