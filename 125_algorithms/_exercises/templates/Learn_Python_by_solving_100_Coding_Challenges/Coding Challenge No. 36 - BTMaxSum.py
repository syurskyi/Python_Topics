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


c_ TreeNode:
    ___  - , x:
        val _ x
        left _ N..
        right _ N..

c_ Solution:
    # @param root, a tree node
    # @return an integer
    ___ maxPathSum , root:
        maxValue _ fl.. "-inf"
        maxPathSumRec root
        r_ maxValue

    ___ maxPathSumRec , root:
        __ root __ N..:
            r_ 0
        leftSum _ maxPathSumRec root.left
        rightSum _ maxPathSumRec root.right
        __ leftSum<0 an. rightSum<0:
            maxValue _ ma. maxValue, root.val
            r_ root.val
        __ leftSum>0 an. rightSum>0:
            maxValue _ ma. maxValue, root.val+leftSum+rightSum
        maxValueUp _ ma. leftSum, rightSum +root.val
        maxValue _ ma. maxValue, maxValueUp
        r_ maxValueUp


__  -n __ ______
    BT, BT.right, BT.left _ TreeNode 1, TreeNode 2, TreeNode 3
    print   Solution .maxPathSum BT