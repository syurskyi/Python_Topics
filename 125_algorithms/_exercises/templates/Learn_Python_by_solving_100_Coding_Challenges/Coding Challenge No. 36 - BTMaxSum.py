# Binary Tree Maximum Path Sum
# Question: Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.
# For example:
# Given the below binary tree,
# 1
# / \
# 2 3
# Return 6.
# Solutions:


class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ maxPathSum(self, root):
        self.maxValue = float("-inf")
        self.maxPathSumRec(root)
        r_ self.maxValue

    ___ maxPathSumRec(self, root):
        if root == None:
            r_ 0
        leftSum = self.maxPathSumRec(root.left)
        rightSum = self.maxPathSumRec(root.right)
        if leftSum<0 and rightSum<0:
            self.maxValue = ma.(self.maxValue, root.val)
            r_ root.val
        if leftSum>0 and rightSum>0:
            self.maxValue = ma.(self.maxValue, root.val+leftSum+rightSum)
        maxValueUp = ma.(leftSum, rightSum) +root.val
        self.maxValue = ma.(self.maxValue, maxValueUp)
        r_ maxValueUp


if  -n == '__main__':
    BT, BT.right, BT.left = TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution().maxPathSum(BT) )