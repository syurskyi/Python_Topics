# Balanced Binary Tree
# Question: Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1
# Solutions:


c_ TreeNode:
    ___  - , x:
        val _ x
        left _ N..
        right _ N..


c_ Solution:
    # @param root, a tree node
    # @return a boolean
    ___ isBalanced , root:
        r_ isBalancedInt root>_0

    ___ isBalancedInt , root:
        __ root __ N..:
            r_ 0;
        left _ isBalancedInt root.left
        right _ isBalancedInt root.right
        __ left<0 o. right<0 o. ab. left-right>1:
            r_ -1
        r_ ma. left,right+1

__  -n __ ______
    BT, BT.right, BT.right.left _ TreeNode 1, TreeNode 2, TreeNode 3
    print   Solution .isBalanced BT 