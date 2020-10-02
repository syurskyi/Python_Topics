# Minimum Depth of Binary Tree
# Question: Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Solutions:


c_ TreeNode:
    ___  - , x:
        val _ x
        left _ N..
        right _ N..


c_ Solution:
    # @param root, a tree node
    # @return an integer
    ___ minDepth , root:
        __ root __ N..:
            r_ 0
        __ root.left __ N..:
            r_ minDepth root.right + 1
        __ root.right __ N..:
            r_ minDepth root.left + 1
        r_ mi. minDepth root.left,minDepth root.right+1


__  -n __ ______
    BT, BT.right, BT.right.left, BT.left _ TreeNode 1, TreeNode 2, TreeNode 3, TreeNode 10
    print   Solution .minDepth BT 