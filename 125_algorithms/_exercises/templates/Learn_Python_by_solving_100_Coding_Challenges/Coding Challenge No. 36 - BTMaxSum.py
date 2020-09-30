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
        self.val _ x
        self.left _ None
        self.right _ None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ maxPathSum(self, root):
        self.maxValue _ float("-inf")
        self.maxPathSumRec(root)
        r_ self.maxValue

    ___ maxPathSumRec(self, root):
        __ root __ None:
            r_ 0
        leftSum _ self.maxPathSumRec(root.left)
        rightSum _ self.maxPathSumRec(root.right)
        __ leftSum<0 an. rightSum<0:
            self.maxValue _ ma.(self.maxValue, root.val)
            r_ root.val
        __ leftSum>0 an. rightSum>0:
            self.maxValue _ ma.(self.maxValue, root.val+leftSum+rightSum)
        maxValueUp _ ma.(leftSum, rightSum) +root.val
        self.maxValue _ ma.(self.maxValue, maxValueUp)
        r_ maxValueUp


__  -n __ '__main__':
    BT, BT.right, BT.left _ TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution().maxPathSum(BT) )