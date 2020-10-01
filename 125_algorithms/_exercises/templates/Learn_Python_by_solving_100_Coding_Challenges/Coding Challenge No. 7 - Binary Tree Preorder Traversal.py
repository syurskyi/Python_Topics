# Return Binary Pre-order Traversal
# Question: Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree
# 1
# \
# 2
# /
# 3
# return [1,2,3].
# Solutions:

c_ TreeNode:
    ___  -(, x):
        val _ x
        left _ N..
        right _ N..

c_ Solution:
    ___ preorderTraversal(root):
        result _   # list
        stack _ [root]

        w___ stack:
            node _ stack.p..()
            __ node:
                result.ap..(node.val)
                stack.ap..(node.right)
                stack.ap..(node.left)
        r_ result

__  -n __ '__main__':
    BT, BT.right, BT.right.left _ TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution.preorderTraversal(BT) )